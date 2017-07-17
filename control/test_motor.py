import unittest
from motor import Motor



class TestControl(unittest.TestCase):
    def test_should_return_on_engine(self):
        shoulder=Motor()
        shoulder.on()
        self.assertEqual(True,shoulder.Left)
        self.assertEqual(False,shoulder.Right)

if __name__ == '__main__':
  unittest.main()
