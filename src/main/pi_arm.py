import sys
sys.path.append('../../')

from src.main.pin import Pin
from src.main.Infra.rpiexecutor import RPiExecutor
from src.main.logic.control import Control
from src.main.motor import Motor
from src.main.configuration.configuration import Configuration
from src.main.arm import Arm

Configuration().configure()
executor = RPiExecutor()

waist = Motor(13, 19)
shoulder = Motor(23, 24)
elbow = Motor(17, 27)
wrist = Motor(16, 20)
gripper = Motor(5, 6)
led = Pin(21)

arm = Arm(waist, shoulder, elbow, wrist, gripper, led)

while True:

    print "Enter a Junture :"
    junture = raw_input(" < w | s | e | u | g | l > : ")
    print "Enter a direction"
    direction = raw_input("< l | r > < u | d > < o | c > < n | f > : ")
    angle = raw_input("enter an angle <int> : ")

    motor = arm.get_motor(junture)
    control = Control(motor, executor, led)

    if direction == "l":
        control.turn_left(float(angle))
    elif direction == "r":
        control.turn_right(float(angle))
    if direction == "u":
        control.turn_left(float(angle))
    elif direction == "d":
        control.turn_right(float(angle))
    if direction == "o":
        control.turn_left(float(angle))
    elif direction == "c":
        control.turn_right(float(angle))
    elif direction == "n":
        control.turn_on_led()
    elif direction == "f":
        control.turn_off_led()
    else:
        print "choose junture an direction again ."

