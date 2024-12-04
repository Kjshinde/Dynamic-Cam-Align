from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo
from time import sleep

factory = PiGPIOFactory(host='172.20.10.2')
servo = AngularServo(17,min_pulse_width=0.65/1000, max_pulse_width=2.4/1000,pin_factory=factory)

while True:
    servo.angle = 90
    sleep(1)
    servo.angle = -90
    sleep(1)


