import unittest

from src.main.domain.horizontal_joint import HorizontalJoint
from src.main.domain.motor import Motor


class TestArmPartial(unittest.TestCase):
    def should_move_shoulder_left(self):
        current_joint_id = "w"
        current_joint_name = "waist"
        current_motor = Motor(1, 2)
        current_encoder_value = 60

        joint = HorizontalJoint(current_joint_id, current_joint_name, current_motor, current_encoder_value)

    if __name__ == '__main__':
        unittest.main()
