import sys

sys.path.append('../../')

from src.main.domain.pin import Pin
from src.main.logic.parser import Parser
from src.main.Infra.rpiexecutor import RPiExecutor
from src.main.logic.control import Control
from src.main.domain.motor import Motor
from src.main.configuration.configuration import Configuration
from src.main.domain.arm_partial import Arm_partial

Configuration().configure()
executor = RPiExecutor()

waist = Motor(13, 19)
shoulder = Motor(23, 24)
elbow = Motor(17, 27)
wrist = Motor(16, 20)
gripper = Motor(5, 6)
led = Pin(21)

arm = Arm_partial(waist, shoulder, elbow, wrist, gripper, led)

while True:
    primitive_joints = raw_input("enter a joints <(name direction value) ... > : ")

    parser = Parser()
    joints = parser.get_joints(primitive_joints)

    for joint in joints:
        motor = arm.get_motor(joint.name)

        print "direction :" + joint.direction

        control = Control(motor, executor, led)

        if joint.direction == "l":
            control.turn_left(float(joint.value))
        elif joint.direction == "r":
            control.turn_right(float(joint.value))
        if joint.direction == "u":
            control.turn_left(float(joint.value))
        elif joint.direction == "d":
            control.turn_right(float(joint.value))
        if joint.direction == "o":
            control.turn_left(float(joint.value))
        elif joint.direction == "c":
            control.turn_right(float(joint.value))
        elif joint.direction == "n":
            control.turn_on_led()
        elif joint.direction == "f":
            control.turn_off_led()
        else:
            print "choose junture an direction again ."
