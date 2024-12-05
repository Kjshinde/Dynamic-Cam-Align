from gpiozero import LED

from gpiozero.pins.pigpio import PiGPIOFactory

from time import sleep

factory = PiGPIOFactory(host='172.20.10.2')

red = LED(22,pin_factory=factory)

while True:

    red.on()
    print("on")

    sleep(1)

    red.off()
    print("off")

    sleep(1)

   