import unittest

from src.main.domain.joint import Joint
from src.main.logic.parser import Parser


class TestParser(unittest.TestCase):

    def test_should_return_joint(self):
        expected_joint = Joint("w", "o", 10)
        parser = Parser()
        primitive_joint = "w o 10"
        current_join = parser.to_joint(primitive_joint)

        self.assertEquals(current_join.name, expected_joint.name)
        self.assertEquals(current_join.direction, expected_joint.direction)
        self.assertEquals(current_join.value, expected_joint.value)

    def test_should_return_joints(self):
        expected_joints_number = 4
        joints_input = "w l 10 - w r 10 - s u 10 - s d 10"
        parser = Parser()
        current_joints = parser.get_joints(joints_input)

        self.assertEquals(len(current_joints), expected_joints_number)

    def test_should_return_joints(self):
        joints_input = "w l 10 - w r 10"
        parser = Parser()
        current_joints = parser.get_joints(joints_input)

        self.assertEquals(current_joints[0].name, "w")
        self.assertEquals(current_joints[0].direction, "l")
        self.assertEquals(current_joints[0].value, 10)

        self.assertEquals(current_joints[1].name, "w")
        self.assertEquals(current_joints[1].direction, "r")
        self.assertEquals(current_joints[1].value, 10)

if __name__ == '__main__':
    unittest.main()

