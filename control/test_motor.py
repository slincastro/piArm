import unittest
from motor import Motor



class TestControl(unittest.TestCase):
    def test_should_turn_left(self):
        shoulder=Motor()
        shoulder.Left()
        self.assertEqual(True,shoulder.InputA)
        self.assertEqual(False,shoulder.InputB)

    def test_should_turn_right(self):
        shoulder=Motor()
        shoulder.Right()
        self.assertEqual(True,shoulder.InputB)
        self.assertEqual(False,shoulder.InputA)

    def test_should_turn_Left_and_then_turn_right(self):
        shoulder=Motor()

        shoulder.Right()
        self.assertEqual(True,shoulder.InputB)
        self.assertEqual(False,shoulder.InputA)

        shoulder.Left()
        self.assertEqual(True,shoulder.InputA)
        self.assertEqual(False,shoulder.InputB)


if __name__ == '__main__':
  unittest.main()
