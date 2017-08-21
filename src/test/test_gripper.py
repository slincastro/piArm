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

if __name__ == '__main__':
    unittest.main()
