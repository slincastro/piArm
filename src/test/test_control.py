import sys
import unittest
#from unittest.mock import MagicMock
from mock import MagicMock
sys.path.append('../../')
from src.main.motor import Motor
from src.main.logic.control import Control
from src.main.logic.converter import Converter
from src.test.configuration.configuration_test import Configuration
from src.main.Infra.executor import Executor


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

    def test_should_turn_left_02_seconds(self):
        executor = Executor()
        motor = Motor(0, 0)
        motor.left = MagicMock()
        motor.stop = MagicMock()

        control = Control(motor, executor)
        executor.move = MagicMock()
        control.turn_left(10)

        executor.move.assert_called_with(motor, 10)
        motor.left.assert_called_with()
        motor.stop.assert_called_with()

if __name__ == '__main__':
    unittest.main()