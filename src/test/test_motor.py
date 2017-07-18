import sys
sys.path.append('../../')
import unittest
from src.main.motor import Motor


class TestMotor(unittest.TestCase):

    def test_should_turn_left(self):
        shoulder = Motor()
        shoulder.left()
        self.assertEqual(True, shoulder.input_a)
        self.assertEqual(False, shoulder.input_b)

    def test_should_turn_right(self):
        shoulder = Motor()
        shoulder.right()
        self.assertEqual(True, shoulder.input_b)
        self.assertEqual(False, shoulder.input_a)

    def test_should_turn_Left_and_then_turn_right(self):
        shoulder = Motor()

        shoulder.right()
        self.assertEqual(True, shoulder.input_b)
        self.assertEqual(False, shoulder.input_a)

        shoulder.left()
        self.assertEqual(True, shoulder.input_a)
        self.assertEqual(False, shoulder.input_b)

    def test_should_stop_motor(self):
        motor = Motor()
        motor.left()
        motor.stop()
        self.assertEqual(False, motor.input_a)
        self.assertEqual(False, motor.input_b)

if __name__ == '__main__':
    unittest.main()
