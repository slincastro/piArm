import sys

sys.path.append('../../')

from src.main.logic.parser import Parser
from src.main.domain.pin import Pin
from src.main.Infra.rpiexecutor import RPiExecutor
from src.main.logic.control import Control
from src.main.domain.motor import Motor
from src.main.configuration.configuration import Configuration
from src.main.domain.arm import Arm


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

        arm = Arm(waist, shoulder, elbow, wrist, gripper, led)
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

    def main(self):
        print "Enter a Junture :"
        junture = raw_input(" < w | s | e | u | g | l > : ")
        print "Enter a direction"
        direction = raw_input("< l | r > < u | d > < o | c > < n | f > : ")
        angle = raw_input("enter an angle <int> : ")

        motor = self._arm.get_motor(junture)
        control = Control(motor, self._executor, self._led)

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

if __name__ == '__main__':
    piarm = PiArm(None)

    while True:
        primitive_joints = raw_input("enter a joints <(name direction value) ... > : ")

        parser = Parser()
        joints = parser.get_joints(primitive_joints)

        for joint in joints:
            piarm.execute_joint(joint)


