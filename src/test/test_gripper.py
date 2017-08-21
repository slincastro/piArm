import unittest

from src.main.domain.gripper import Gripper
from src.main.domain.motor import Motor


class TestJoint(unittest.TestCase):
    def test_should_return_gripper(self):
        gripper_motor = Motor(1, 2)

        gripper = Gripper(gripper_motor)

        expected_motor = Motor(1, 2)

        self.assertEquals(gripper.motor, expected_motor)
        self.assertFalse(gripper.has_gripped())

    def test_should_gripped(self):
        gripper_motor = Motor(1, 2)

        gripper = Gripper(gripper_motor)

        gripper.gripped()

        self.assertTrue(gripper.has_gripped())

    def test_should_close_gripper(self):
        gripper_motor = Motor(1, 2)

        gripper = Gripper(gripper_motor)

        gripper.close()

        self.assertTrue(gripper.motor._is_on)

    def test_should_open_gripper(self):
        gripper_motor = Motor(1, 2)

        gripper = Gripper(gripper_motor)

        gripper.open()

        self.assertTrue(gripper.motor._is_on)

    def test_should_griped(self):
        gripper_motor = Motor(1, 2)

        gripper = Gripper(gripper_motor)

        gripper.close()

        self.assertTrue(gripper.motor.is_on())

        gripper.gripped()

        self.assertFalse(gripper.motor.is_on())

if __name__ == '__main__':
    unittest.main()
