import sys

sys.path.append('../../')

from src.main.logic.parser import Parser
from src.main.domain.pin import Pin
from src.main.Infra.rpiexecutor import RPiExecutor
from src.main.logic.control import Control
from src.main.domain.motor import Motor
from src.main.configuration.configuration import Configuration
from src.main.domain.arm_partial import Arm_partial


class PiArm:

    def __init__(self, control):
        Configuration().configure()
        self._executor = RPiExecutor()

        waist = Motor(13, 19)
        shoulder = Motor(23, 24)
        elbow = Motor(17, 27)
        wrist = Motor(16, 20)
        gripper = Motor(5, 6)
        led = Pin(21)

        arm = Arm_partial(waist, shoulder, elbow, wrist, gripper, led)
        self._arm = arm
        self._led = led

        if control == None :
            print "runtime constructor"
            self._control = Control(None, self._executor, self._led)

        else:
            print "test constructor"
            self._control = control

    def execute_joint(self, joint):

        motor = self._arm.get_motor(joint.name)
        self._control.set_motor(motor)

        control = self._control

        print "direction :" + joint.direction

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

    def parse_joints(self, primitive_joints):
        parser = Parser()
        joints = parser.get_joints(primitive_joints)

        for joint in joints:
            self.execute_joint(joint)


if __name__ == '__main__':  # pragma: no cover
    piarm = PiArm(None)

    while True:
        input_primitive_joints = raw_input("enter a joints <(name direction value) ... > : ")
        piarm.parse_joints(input_primitive_joints)



