import sys
sys.path.append('../../')
import unittest
from src.main.domain.pin import Pin


class TestPin(unittest.TestCase):

    def test_should_return_pin_led(self):
        expected_pin = 1
        pin = Pin(1)
        current_pin = pin.number

        self.assertEquals(current_pin, expected_pin)

    def test_should_return_true(self):
        expected_value = False
        pin = Pin(1)
        current_value = pin.value

        self.assertEquals(current_value, expected_value)

    def test_should_return_true_when_call_on(self):
        pin = Pin(1)
        pin.on()

        self.assertTrue(pin.value)

    def test_should_return_true_when_call_off(self):
        pin = Pin(1)
        pin.off()

        self.assertFalse(pin.value)

if __name__ == '__main__':
    unittest.main()
