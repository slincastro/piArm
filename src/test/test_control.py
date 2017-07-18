import unittest
import sys
sys.path.append('../../')
from src.main.control import Control
from src.main.motor import Motor
from src.main.converter import Converter
from configuration_test import Configuration


class TestControl(unittest.TestCase):

    def setUp(self):
        config = Configuration()
        config.configure_test()

    def test_should_return_01_seconds(self):
        convert = Converter()
        seconds = convert.to_seconds(10)
        self.assertEqual(0.1, seconds)

    def test_should_return_02_seconds(self):
        convert = Converter()
        seconds = convert.to_seconds(20)
        self.assertEqual(0.2, seconds)


if __name__ == '__main__':
    unittest.main()
