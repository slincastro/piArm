import sys
sys.path.append('../../')
import unittest
from src.main.domain.motor import Motor


class TestMotor(unittest.TestCase):

    def test_should_turn_left(self):
        shoulder = Motor(0, 0)
        shoulder.turn_left()
        self.assertEqual(True, shoulder.pin_a.value)
        self.assertEqual(False, shoulder.pin_b.value)

    def test_should_turn_right(self):
        shoulder = Motor(0, 0)
        shoulder.turn_right()
        self.assertEqual(True, shoulder.pin_b.value)
        self.assertEqual(False, shoulder.pin_a.value)

    def test_should_turn_Left_and_then_turn_right(self):
        shoulder = Motor(0, 0)

        shoulder.turn_right()
        self.assertEqual(True, shoulder.pin_b.value)
        self.assertEqual(False, shoulder.pin_a.value)

        shoulder.turn_left()
        self.assertEqual(True, shoulder.pin_a.value)
        self.assertEqual(False, shoulder.pin_b.value)

    def test_should_stop_motor(self):
        motor = Motor(0, 0)
        motor.turn_left()
        motor.stop()
        self.assertEqual(False, motor.pin_a.value)
        self.assertEqual(False, motor.pin_b.value)

    def test_should_be_pin1_and2_when_configure_motor(self):
        motor = Motor(1, 2)

        self.assertEqual(1, motor.pin_a.number)
        self.assertEqual(2, motor.pin_b.number)

if __name__ == '__main__':
    unittest.main()
