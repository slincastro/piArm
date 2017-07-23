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
elbow = Motor(17, 27)
wrist = Motor(16, 20)
gripper = Motor(5, 6)

arm = Arm(waist, shoulder, elbow, wrist, gripper)

while True:
    junture = raw_input("enter an junture <w>: ")
    direction = raw_input("enter a direction <l|r>")

    motor = arm.get_motor(junture)
    control = Control(motor, executor)

    if direction == "^[[A":
        control.turn_left(float(10))
    elif direction == "^[[B":
        control.turn_right(float(10))
    else:
        print "choose junture an direction again ."

