import cv2
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# Initialize video capture from webcam
cap = cv2.VideoCapture(0)

# Create a CSRT tracker object
tracker = cv2.TrackerCSRT_create()

# Read the first frame from the video
ret, frame = cap.read()

# Select the bounding box on the first frame for the object you want to track
bbox = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)

# Initialize the tracker with the first frame and bounding box
tracker.init(frame, bbox)

# Setup remote GPIO for servo control
factory = PiGPIOFactory(host='172.20.10.2')
horizontal_servo = AngularServo(17, min_pulse_width=0.65/1000, max_pulse_width=2.4/1000, pin_factory=factory)
vertical_servo = AngularServo(27, min_pulse_width=0.65/1000, max_pulse_width=2.4/1000, pin_factory=factory)

# Initial servo positions (centered)
horizontal_servo.angle = 0
vertical_servo.angle = 0

try:
    while True:
        # Read a new frame
        ret, frame = cap.read()
        if not ret:
            break

        # Update the tracker on the new frame
        success, bbox = tracker.update(frame)

        # Calculate center of the bounding box
        if success:
            (x, y, w, h) = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Calculate center of object
            object_center_x = x + w / 2
            object_center_y = y + h / 2
            
            # Calculate deviation from center of frame
            frame_center_x = frame.shape[1] / 2
            frame_center_y = frame.shape[0] / 2
            
            horizontal_deviation = object_center_x - frame_center_x
            vertical_deviation = object_center_y - frame_center_y
            
            # Adjust horizontal servo angle based on deviation
            if abs(horizontal_deviation) > 20:  # Threshold to prevent jittering
                new_horizontal_angle = horizontal_servo.angle + horizontal_deviation * 0.1
                
                # Ensure new_angle is within valid range [-90, 90]
                new_horizontal_angle = max(-90, min(90, new_horizontal_angle))
                
                horizontal_servo.angle = new_horizontal_angle
            
            # Adjust vertical servo angle based on deviation
            if abs(vertical_deviation) > 20:  # Threshold to prevent jittering
                new_vertical_angle = vertical_servo.angle - vertical_deviation * 0.1
                
                # Ensure new_angle is within valid range [-90, 90]
                new_vertical_angle = max(-90, min(90, new_vertical_angle))
                
                vertical_servo.angle = new_vertical_angle

        else:
            cv2.putText(frame, "Tracking failure detected", (100, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Display the result
        cv2.imshow("Tracking", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Release resources
    cap.release()
    cv2.destroyAllWindows()