import RPi.GPIO as GPIO


class RPiExecutor:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def move(self, motor):

        print "move ...."
        print "pin a :" + str(motor.pin_a)
        print "pin b :" + str(motor.pin_b)

        GPIO.setup(motor.pin_a, GPIO.OUT)
        GPIO.setup(motor.pin_b, GPIO.OUT)
        GPIO.output(motor.pin_a, motor.input_a)
        GPIO.output(motor.pin_b, motor.input_b)

    def go(self, pin):
        GPIO.setup(pin.pin_number, GPIO.OUT)
        GPIO.output(pin.pin_number, pin.pin_value)



