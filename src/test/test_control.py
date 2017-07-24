import sys
import unittest

from mock import MagicMock

sys.path.append('../../')
from src.main.domain.motor import Motor
from src.main.logic.control import Control
from src.main.logic.converter import Converter
from src.test.configuration.configuration_test import Configuration
from src.main.Infra.rpiexecutor import RPiExecutor
from src.main.domain.pin import Pin


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

    def test_should_turn_left_02_degrees(self):
        executor = RPiExecutor()
        motor = Motor(0, 0)
        control = Control(motor, executor, None)

        motor.left = MagicMock()
        motor.stop = MagicMock()
        executor.move = MagicMock()

        control.turn_left(10)

        executor.move.assert_called_with(motor)
        motor.left.assert_called_with()
        motor.stop.assert_called_with()

    def test_should_turn_right_02_degrees(self):
        executor = RPiExecutor()
        motor = Motor(0, 0)
        control = Control(motor, executor, None)

        motor.right = MagicMock()
        motor.stop = MagicMock()
        executor.move = MagicMock()

        control.turn_right(10)

        executor.move.assert_called_with(motor)
        motor.right.assert_called_with()
        motor.stop.assert_called_with()

    def test_should_turn_on_led(self):
        executor = RPiExecutor()
        pin = Pin(21)

        pin.on = MagicMock()
        executor.go = MagicMock()

        control = Control(None, executor, pin)

        control.turn_on_led()

        pin.on.assert_called_with()
        executor.go.assert_called_with(pin)

    def test_should_turn_off_led(self):
        executor = RPiExecutor()
        pin = Pin(21)

        pin.off = MagicMock()
        executor.go = MagicMock()

        control = Control(None, executor, pin)

        control.turn_off_led()

        pin.off.assert_called_with()
        executor.go.assert_called_with(pin)

if __name__ == '__main__':
    unittest.main()
