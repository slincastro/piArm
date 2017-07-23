import sys
sys.path.append('../../')
from src.main.Infra.executor import Executor
from src.main.logic.control import Control
from src.main.motor import Motor
from src.main.configuration.configuration import Configuration
from src.main.arm import Arm

Configuration().configure()
executor = Executor()
waist = Motor(13, 19)
shoulder = Motor(23, 24)
arm = Arm(waist, shoulder)

while True:
    junture = raw_input("enter an junture <w>: ")
    angle = raw_input("enter an angle <int>: ")
    direction = raw_input("enter a direction <l|r>")

    motor = arm.get_motor(junture)
    control = Control(motor, executor)

    if direction == "l":
        control.turn_left(float(angle))
    elif direction == "r":
        control.turn_right(float(angle))
    else:
        print "choose junture an direction again ."

