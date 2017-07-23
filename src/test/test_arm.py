import sys
sys.path.append('../../')
import unittest
from src.main.motor import Motor
from src.main.arm import Arm


class TestArm(unittest.TestCase):

    def test_should_return_waist(self):
        expected_motor = Motor(13, 19)
        waist = Motor(13, 19)
        arm = Arm(waist, None)

        self.assertEquals(expected_motor.input_a, arm.waist.input_a)
        self.assertEquals(expected_motor.input_b, arm.waist.input_b)
        self.assertEquals(expected_motor.pin_a, arm.waist.pin_a)
        self.assertEquals(expected_motor.pin_b, arm.waist.pin_b)

    def test_should_return_waist_motor(self):
        expected_motor = Motor(13, 19)
        waist = Motor(13, 19)
        arm = Arm(waist, None)

        current_waist = arm.get_motor("w")

        self.assertEquals(expected_motor.input_a, current_waist.input_a)
        self.assertEquals(expected_motor.input_b, current_waist.input_b)
        self.assertEquals(expected_motor.pin_a, current_waist.pin_a)
        self.assertEquals(expected_motor.pin_b, current_waist.pin_b)

    def test_should_return_shoulder_motor(self):
        expected_motor = Motor(23, 24)
        shoulder = Motor(23, 24)
        arm = Arm(None, shoulder)

        current_waist = arm.get_motor("s")

        self.assertEquals(expected_motor.input_a, current_waist.input_a)
        self.assertEquals(expected_motor.input_b, current_waist.input_b)
        self.assertEquals(expected_motor.pin_a, current_waist.pin_a)
        self.assertEquals(expected_motor.pin_b, current_waist.pin_b)

    def test_should_return_none_motor(self):
        waist = Motor(13, 19)
        arm = Arm(waist, None)

        current_waist = arm.get_motor("x")

        self.assertIsNone(current_waist)

