import RPi.GPIO as GPIO
import time


class Executor:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def move(self, motor, seconds):
        GPIO.setup(motor.pin_a, GPIO.OUT)
        GPIO.setup(motor.pin_b, GPIO.OUT)
        GPIO.output(motor.pin_a, motor.input_a)
        time.sleep(seconds)
