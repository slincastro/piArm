import unittest
import sys
sys.path.append('../../')
from src.main.control import Control
from src.main.motor import Motor


class TestControl(unittest.TestCase):


    def test_should_move_10_degrees_left(self):
        motor = Motor()
        move = Control(motor)
        move.turn_left(10)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
