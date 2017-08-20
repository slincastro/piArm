import unittest

from src.main.domain.encoder import Encoder
from src.main.domain.horizontal_joint import HorizontalJoint
from src.main.domain.motor import Motor


class TestHorizontalJoint(unittest.TestCase):
    def test_should_move_left_when_encoder_Value_less_than_150(self):
        current_joint_id = "w"
        current_joint_name = "waist"
        current_motor = Motor(1, 2)
        current_encoder_value = 60

        joint = HorizontalJoint(current_joint_id, current_joint_name, current_motor, current_encoder_value)

        joint.left()

        self.assertTrue(joint.motor.is_on())

    def test_should_stop_when_encoder_value_equals_150(self):
        current_joint_id = "w"
        current_joint_name = "waist"
        current_motor = Motor(1, 2)
        current_encoder_value = 150

        joint = HorizontalJoint(current_joint_id, current_joint_name, current_motor, current_encoder_value)

        joint.left()

        self.assertFalse(joint.motor.is_on())

    def test_should_stop_when_encoder_value_more_than_150(self):
        current_joint_id = "w"
        current_joint_name = "waist"
        current_motor = Motor(1, 2)
        current_encoder_value = 151

        joint = HorizontalJoint(current_joint_id, current_joint_name, current_motor, current_encoder_value)

        joint.left()

        self.assertFalse(joint.motor.is_on())

    def test_should_move_right_when_encoder_Value_less_than_150(self):
        current_joint_id = "w"
        current_joint_name = "waist"
        current_motor = Motor(1, 2)
        current_encoder_value = 60

        joint = HorizontalJoint(current_joint_id, current_joint_name, current_motor, current_encoder_value)

        joint.right()

        self.assertTrue(joint.motor.is_on())

    def test_should_rigth_and_stop_when_encoder_value_equals_150(self):
        current_joint_id = "w"
        current_joint_name = "waist"
        current_motor = Motor(1, 2)
        current_encoder_value = 150

        joint = HorizontalJoint(current_joint_id, current_joint_name, current_motor, current_encoder_value)

        joint.right()

        self.assertFalse(joint.motor.is_on())

    def test_should_right_and_stop_when_encoder_value_more_than_150(self):
        current_joint_id = "w"
        current_joint_name = "waist"
        current_motor = Motor(1, 2)
        current_encoder_value = 151

        joint = HorizontalJoint(current_joint_id, current_joint_name, current_motor, current_encoder_value)

        joint.right()

        self.assertFalse(joint.motor.is_on())


if __name__ == '__main__':
    unittest.main()
