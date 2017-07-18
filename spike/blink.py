import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

led=21
GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(led, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

##Define a function named Blink()
def Blink(numTimes,speed):
    for i in range(0,numTimes):## Run loop numTimes
        print "Iteration " + str(i+1)## Print current loop
        GPIO.output(led,True)## Switch on pin 7
        time.sleep(speed)## Wait
        GPIO.output(led,False)## Switch off pin 7
        time.sleep(speed)## Wait
        print "Done" ## When loop is complete, print "Done"
        ##GPIO.cleanup()

## Ask user for total number of blinks and length of each blink
iterations = raw_input("Enter total number of times to blink: ")
speed = raw_input("Enter length of each blink(seconds): ")

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
Blink(int(iterations),float(speed))
