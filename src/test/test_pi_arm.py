import sys
import unittest
from mock import MagicMock

sys.path.append('../../')

from src.main.Infra.rpiexecutor import RPiExecutor
from src.main.logic.control import Control
from src.test.configuration.configuration_test import Configuration
from src.main.domain.arm import Arm
from src.main.domain.joint import Joint
from src.main.pi_arm import PiArm
from src.main.domain.pin import Pin
from src.main.domain.motor import Motor


class TestPiArm(unittest.TestCase):

    def test_should_configure_arm(self):
        expected_waist = Motor(13, 19)
        expected_shoulder = Motor(23, 24)
        expected_elbow = Motor(17, 27)
        expected_wrist = Motor(16, 20)
        expected_gripper = Motor(5, 6)
        expected_led = Pin(21)

        expected_arm = Arm(expected_waist, expected_shoulder, expected_elbow, expected_wrist, expected_gripper, expected_led)

        pi_arm = PiArm(None)
        current_arm = pi_arm._arm

        self.assertEquals(current_arm.waist.pin_a.number, expected_arm.waist.pin_a.number)
        self.assertEquals(current_arm.waist.pin_b.number, expected_arm.waist.pin_b.number)
        self.assertEquals(current_arm.shoulder.pin_a.number, expected_arm.shoulder.pin_a.number)
        self.assertEquals(current_arm.shoulder.pin_b.number, expected_arm.shoulder.pin_b.number)
        self.assertEquals(current_arm.elbow.pin_a.number, expected_arm.elbow.pin_a.number)
        self.assertEquals(current_arm.elbow.pin_b.number, expected_arm.elbow.pin_b.number)
        self.assertEquals(current_arm.wrist.pin_a.number, expected_arm.wrist.pin_a.number)
        self.assertEquals(current_arm.wrist.pin_b.number, expected_arm.wrist.pin_b.number)
        self.assertEquals(current_arm.gripper.pin_a.number, expected_arm.gripper.pin_a.number)
        self.assertEquals(current_arm.gripper.pin_b.number, expected_arm.gripper.pin_b.number)
        self.assertEquals(current_arm.led.number, expected_arm.led.number)

    def test_should_execute_waist_left(self):

        input_joint = Joint("w", "l", 10)
        expected_joint_value = float(10)

        control, pi_arm = self.pi_arm_configuration()
        control.turn_left = MagicMock()
        pi_arm.execute_joint(input_joint)

        control.turn_left.assert_called_with(expected_joint_value)

    def test_should_execute_waist_right(self):

        input_joint = Joint("w", "r", 10)
        expected_joint_value = float(10)

        control, pi_arm = self.pi_arm_configuration()
        control.turn_right = MagicMock()

        pi_arm.execute_joint(input_joint)

        control.turn_right.assert_called_with(expected_joint_value)

    def test_should_execute_gripper_open(self):
        input_joint = Joint("g", "o", 10)
        expected_joint_value = float(10)

        control, pi_arm = self.pi_arm_configuration()
        control.turn_left = MagicMock()

        pi_arm.execute_joint(input_joint)

        control.turn_left.assert_called_with(expected_joint_value)

    def test_should_execute_gripper_close(self):
        input_joint = Joint("g", "c", 10)
        expected_joint_value = float(10)

        control, pi_arm = self.pi_arm_configuration()
        control.turn_right = MagicMock()

        pi_arm.execute_joint(input_joint)

        control.turn_right.assert_called_with(expected_joint_value)

    def test_should_execute_elbow_down(self):
        input_joint = Joint("e", "d", 10)
        expected_joint_value = float(10)

        control, pi_arm = self.pi_arm_configuration()
        control.turn_right = MagicMock()

        pi_arm.execute_joint(input_joint)

        control.turn_right.assert_called_with(expected_joint_value)

    def test_should_execute_elbow_up(self):
        input_joint = Joint("e", "u", 10)
        expected_joint_value = float(10)

        control, pi_arm = self.pi_arm_configuration()
        control.turn_left = MagicMock()

        pi_arm.execute_joint(input_joint)

        control.turn_left.assert_called_with(expected_joint_value)

    def test_should_execute_led_on(self):
        input_joint = Joint("l", "n", 10)
        expected_joint_value = float(10)

        control, pi_arm = self.pi_arm_configuration()
        control.turn_on_led = MagicMock()

        pi_arm.execute_joint(input_joint)

        control.turn_on_led.assert_called_with()

    def test_should_execute_led_off(self):
        input_joint = Joint("l", "f", 10)
        expected_joint_value = float(10)

        control, pi_arm = self.pi_arm_configuration()
        control.turn_off_led = MagicMock()

        pi_arm.execute_joint(input_joint)

        control.turn_off_led.assert_called_with()

    def should_be_call_parser_with_joint(self):
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
        control = Control(None, self._executor, self._led)
        pi_arm = PiArm(control)

        input_primitive_joints = "g c 10"
        pi_arm.execute_joint = MagicMock()
        expected_joint = Joint("g", "c", 10)

        pi_arm.parse_joints(input_primitive_joints)

        pi_arm.execute_joint.assert_called_with(expected_joint)

    def pi_arm_configuration(self):
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
        control = Control(None, self._executor, self._led)
        pi_arm = PiArm(control)

        return control, pi_arm


if __name__ == '__main__':
    unittest.main()






