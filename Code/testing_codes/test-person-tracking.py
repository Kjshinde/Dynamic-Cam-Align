import cv2

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

while True:
    # Read a new frame
    ret, frame = cap.read()
    if not ret:
        break

    # Update the tracker on the new frame
    success, bbox = tracker.update(frame)

    # Draw the bounding box if tracking was successful
    if success:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Tracking failure detected", (100, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display the result
    cv2.imshow("Tracking", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()