import sys

from src.main.domain.arm import Arm
from src.main.pi_arm import PiArm

sys.path.append('../../')

from src.main.domain.pin import Pin
from src.main.domain.motor import Motor
import unittest


class TestPiArm(unittest.TestCase):

    def test_should_configure_arm(self):
        expected_waist = Motor(13, 19)
        expected_shoulder = Motor(23, 24)
        expected_elbow = Motor(17, 27)
        expected_wrist = Motor(16, 20)
        expected_gripper = Motor(5, 6)
        expected_led = Pin(21)

        expected_arm = Arm(expected_waist, expected_shoulder, expected_elbow, expected_wrist, expected_gripper, expected_led)

        pi_arm = PiArm()
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


    






