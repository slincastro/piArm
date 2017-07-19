import RPi.GPIO as GPIO
import time

class Executor:

    def move(self, motor, degrees):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(motor._pinA, GPIO.OUT)
        GPIO.setup(motor._pinB, GPIO.OUT)

