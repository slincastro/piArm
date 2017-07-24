import unittest

from src.main.domain.joint import Joint
from src.main.domain.motor import Motor


class TestJoint(unittest.TestCase):

    def test_should_return_joint(self):
        expected_motor = Motor(1, 2)
        joint = Joint("w", "l", 10)

        self.assertEquals(joint.name, "w")
        self.assertEquals(joint.direction, "l")
        self.assertEquals(joint.value, 10)
