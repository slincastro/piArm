import sys
sys.path.append('../../')
from src.main.Infra.executor import Executor
from src.main.logic.control import Control
from src.main.motor import Motor
from src.main.configuration.configuration import Configuration

Configuration().configure_test()
executor = Executor()
motor = Motor(0, 0)


while True:
    action = raw_input("enter an action <o|c>: ")
    if action == "w":
        print "waist"
        control = Control(motor, executor)
        control.turn_left(10)



