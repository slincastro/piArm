import unittest

from src.main.domain.joint_partial import Joint_partial
from src.main.domain.motor import Motor


class TestJointPartial(unittest.TestCase):

    def test_should_return_joint(self):
        expected_motor = Motor(1, 2)
        joint = Joint_partial("w", "l", 10)

        current_name = joint.name

        self.assertEquals(current_name, "w")
        self.assertEquals(joint.direction, "l")
        self.assertEquals(joint.value, 10)

if __name__ == '__main__':
    unittest.main()