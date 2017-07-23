import RPi.GPIO as GPIO



class Executor:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def move(self, motor, seconds):

        print "move ...."
        print "pin a :" + str(motor.pin_a)
        print "pin b :" + str(motor.pin_b)
        print "seconds :" + str(seconds)

        GPIO.setup(motor.pin_a, GPIO.OUT)
        GPIO.setup(motor.pin_b, GPIO.OUT)
        GPIO.output(motor.pin_a, motor.input_a)
        GPIO.output(motor.pin_b, motor.input_b)



