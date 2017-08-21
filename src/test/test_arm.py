import sys
import unittest

from src.main.domain.vertical_joint import VerticalJoint

sys.path.append('../../')

from src.main.domain.arm import Arm
from src.main.domain.horizontal_joint import HorizontalJoint
from src.main.domain.motor import Motor


class TestArm(unittest.TestCase):
    def test_should_return_same_waist_joint(self):
        current_joint_id = "w"
        current_joint_name = "waist"
        current_motor = Motor(1, 2)
        current_encoder_value = 60

        waist = HorizontalJoint(current_joint_id, current_joint_name, current_motor, current_encoder_value)

        expected_joint_id = "w"
        expected_joint_name = "waist"
        expected_motor = Motor(1, 2)
        expected_encoder_value = 60

        expected_waist = HorizontalJoint(expected_joint_id, expected_joint_name, expected_motor, expected_encoder_value)

        arm = Arm(waist, None)

        self.assertEquals(arm.waist, expected_waist)

    def test_should_return_same_shoulder_joint(self):
        current_joint_id = "s"
        current_joint_name = "shoulder"
        current_motor = Motor(1, 2)
        current_encoder_value = 60

        shoulder = VerticalJoint(current_joint_id, current_joint_name, current_motor, current_encoder_value)

        expected_joint_id = "s"
        expected_joint_name = "shoulder"
        expected_motor = Motor(1, 2)
        expected_encoder_value = 60

        expected_shoulder = VerticalJoint(expected_joint_id, expected_joint_name, expected_motor,
                                          expected_encoder_value)

        arm = Arm(None, shoulder)

        self.assertEquals(arm.shoulder, expected_shoulder)


if __name__ == '__main__':
    unittest.main()
