import unittest

from src.main.domain.joint import Joint
from src.main.logic.parser import Parser


class TestParser(unittest.TestCase):

    def test_should_return_junture(self):
        expected_joint = Joint("w", "o", 10)
        parser = Parser()
        primitive_joint = "w o 10"
        current_join = parser.to_joint(primitive_joint)

        self.assertEquals(current_join.name, expected_joint.name)
        self.assertEquals(current_join.direction, expected_joint.direction)
        self.assertEquals(current_join.value, expected_joint.value)
