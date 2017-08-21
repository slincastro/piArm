import sys
import unittest

from src.main.domain.vertical_joint import VerticalJoint

sys.path.append('../../')

from src.main.domain.arm import Arm
from src.main.domain.horizontal_joint import HorizontalJoint
from src.main.domain.motor import Motor


class TestArm(unittest.TestCase):
    def test_should_return_waist_joint(self):
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

    def test_should_return_shoulder_joint(self):
        vertical_joints = self.get_vertical_joints()

        expected_shoulder_id = "s"
        expected_shoulder_name = "shoulder"
        expected_motor = Motor(1, 2)
        expected_encoder_value = 60

        expected_shoulder = VerticalJoint(expected_shoulder_id, expected_shoulder_name, expected_motor,
                                          expected_encoder_value)

        arm = Arm(None, vertical_joints)

        self.assertEquals(arm.get_vertical_joint(expected_shoulder_id), expected_shoulder)

    def test_should_return_elbow_joint(self):
        vertical_joints = self.get_vertical_joints()

        expected_elbow_id = "e"
        expected_joint_name = "elbow"
        expected_motor = Motor(1, 2)
        expected_encoder_value = 60

        expected_elbow = VerticalJoint(expected_elbow_id, expected_joint_name, expected_motor,
                                       expected_encoder_value)

        arm = Arm(None, vertical_joints)

        self.assertEquals(arm.get_vertical_joint(expected_elbow_id), expected_elbow)

    def test_should_return_wrist_joint(self):
        vertical_joints = self.get_vertical_joints()

        expected_wrist_id = "u"
        expected_wrist_name = "wrist"
        expected_motor = Motor(1, 2)
        expected_encoder_value = 60

        expected_elbow = VerticalJoint(expected_wrist_id, expected_wrist_name, expected_motor,
                                       expected_encoder_value)

        arm = Arm(None, vertical_joints)

        self.assertEquals(arm.get_vertical_joint(expected_wrist_id), expected_elbow)

    def get_vertical_joints(self):
        current_joint_id = "e"
        current_joint_name = "elbow"
        current_motor = Motor(1, 2)
        current_encoder_value = 60

        elbow = VerticalJoint(current_joint_id, current_joint_name, current_motor, current_encoder_value)

        current_shoulder_joint_id = "s"
        current_shoulder_joint_name = "shoulder"
        current_shoulder_motor = Motor(1, 2)
        current_shoulder_encoder_value = 60

        shoulder = VerticalJoint(current_shoulder_joint_id, current_shoulder_joint_name, current_shoulder_motor,
                                 current_shoulder_encoder_value)

        current_wrist_joint_id = "u"
        current_wrist_joint_name = "wrist"
        current_wrist_motor = Motor(1, 2)
        current_wrist_encoder_value = 60

        wrist = VerticalJoint(current_wrist_joint_id, current_wrist_joint_name, current_wrist_motor,
                              current_wrist_encoder_value)

        vertical_joints = [elbow, shoulder, wrist]

        return vertical_joints


if __name__ == '__main__':
    unittest.main()
