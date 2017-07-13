import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

grippera=5
gripperb=6
juntura=16
junturb=20

GPIO.setmode(GPIO.BCM) 
GPIO.setup(grippera, GPIO.OUT) 
GPIO.setup(gripperb, GPIO.OUT)
GPIO.setup(juntura, GPIO.OUT) 
GPIO.setup(junturb, GPIO.OUT)


def Open(numTimes,speed):
    for i in range(0,numTimes):
        print "Iteration " + str(i+1)

        GPIO.output(grippera,True)
        GPIO.output(gripperb,False)
        time.sleep(speed)
        GPIO.output(grippera,True)
        GPIO.output(gripperb,True)
        time.sleep(speed)
        print "Done"

def Close(numTimes,speed):
    for i in range(0,numTimes):
        print "Iteration " + str(i+1)

        GPIO.output(grippera,False)
        GPIO.output(gripperb,True)
        time.sleep(speed)
        GPIO.output(grippera,True)
        GPIO.output(gripperb,True)
        time.sleep(speed)
        print "Done"

def Up(numTimes,speed):
    for i in range(0,numTimes):
        print "Iteration " + str(i+1)

        GPIO.output(juntura,True)
        GPIO.output(junturb,False)
        time.sleep(speed)
        GPIO.output(juntura,True)
        GPIO.output(junturb,True)
        time.sleep(speed)
        print "Done"

def Down(numTimes,speed):
    for i in range(0,numTimes):
        print "Iteration " + str(i+1)

        GPIO.output(juntura,False)
        GPIO.output(junturb,True)
        time.sleep(speed)
        GPIO.output(juntura,True)
        GPIO.output(junturb,True)
        time.sleep(speed)
        print "Done"
                
iterations = 1#raw_input("Enter total number of times to blink: ")
action = raw_input("enter an action <o|c>: ")

if action == "o":
    Open(int(iterations),float(0.2))
elif action == "c":
    Close(int(iterations),float(0.2))
elif action == "u":
    Up(int(iterations),float(0.2))
elif action == "d":
    Down(int(iterations),float(0.2))
