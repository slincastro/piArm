import unittest

from src.main.domain.joint import Joint
from src.main.domain.motor import Motor


class TestJoint(unittest.TestCase):
    def test_should_return_joint(self):
        expected_joint_id = "w"
        expected_joint_name = "waist"
        expected_motor = Motor(1, 2)
        expected_encoder_value = 250

        current_joint_id = "w"
        current_joint_name = "waist"
        current_motor = Motor(1, 2)
        current_encoder_value = 250

        joint = Joint(current_joint_id, current_joint_name, current_motor, current_encoder_value)

        self.assertEquals(joint.id, expected_joint_id)
        self.assertEquals(joint.name, expected_joint_name)
        self.assertEquals(joint.motor, expected_motor)
        self.assertEquals(joint.encoder, expected_encoder_value)


if __name__ == '__main__':
    unittest.main()
