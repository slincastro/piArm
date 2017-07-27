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

        self.assertEquals(current_arm.waist.pin_a, expected_arm.waist.pin_a)
        self.assertEquals(current_arm.waist.pin_b, expected_arm.waist.pin_b)
        self.assertEquals(current_arm.shoulder.pin_a, expected_arm.shoulder.pin_a)
        self.assertEquals(current_arm.shoulder.pin_b, expected_arm.shoulder.pin_b)
        self.assertEquals(current_arm.elbow.pin_a, expected_arm.elbow.pin_a)
        self.assertEquals(current_arm.elbow.pin_b, expected_arm.elbow.pin_b)
        self.assertEquals(current_arm.wrist.pin_a, expected_arm.wrist.pin_a)
        self.assertEquals(current_arm.wrist.pin_b, expected_arm.wrist.pin_b)
        self.assertEquals(current_arm.gripper.pin_a, expected_arm.gripper.pin_a)
        self.assertEquals(current_arm.gripper.pin_b, expected_arm.gripper.pin_b)
        self.assertEquals(current_arm.led.pin_number, expected_arm.led.pin_number)

    def test_should_execute_waist_left(self):

        input_joint = Joint("w", "l", 10)

        Configuration().configure()
        self._executor = RPiExecutor()
        expected_joint_value = float(10)

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
        control.turn_left = MagicMock()

        pi_arm.execute_joint(input_joint)

        control.turn_left.assert_called_with(expected_joint_value)

    def test_should_execute_waist_right(self):

        input_joint = Joint("w", "r", 10)

        Configuration().configure()
        self._executor = RPiExecutor()
        expected_joint_value = float(10)

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
        control.turn_right = MagicMock()

        pi_arm.execute_joint(input_joint)

        control.turn_right.assert_called_with(expected_joint_value)


if __name__ == '__main__':
    unittest.main()






