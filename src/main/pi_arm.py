import sys
sys.path.append('../../')
from src.main.Infra.executor import Executor
from src.main.logic.control import Control
from src.main.motor import Motor
from src.main.configuration.configuration import Configuration
from src.main.arm import Arm

Configuration().configure_test()
executor = Executor()
waist = Motor(13, 19)
arm = Arm(waist)

while True:
    action = raw_input("enter an junture <o|c>: ")

    motor = arm.get_motor(action)
    control = Control(motor, executor)
    control.turn_left(10)



