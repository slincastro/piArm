import sys
import unittest

sys.path.append('../../')

from src.main.domain.motor import Motor
from src.main.domain.arm import Arm
from src.main.domain.pin import Pin


class TestArm(unittest.TestCase):

    def test_should_return_waist(self):
        expected_motor = Motor(13, 19)
        waist = Motor(13, 19)
        arm = Arm(waist, None, None, None, None, None)

        self.assertEquals(expected_motor.input_a, arm.waist.input_a)
        self.assertEquals(expected_motor.input_b, arm.waist.input_b)
        self.assertEquals(expected_motor.pin_a, arm.waist.pin_a)
        self.assertEquals(expected_motor.pin_b, arm.waist.pin_b)

    def test_should_return_waist_motor(self):
        expected_motor = Motor(13, 19)
        waist = Motor(13, 19)
        arm = Arm(waist, None, None, None, None, None)

        current_waist = arm.get_motor("w")

        self.assertEquals(expected_motor.input_a, current_waist.input_a)
        self.assertEquals(expected_motor.input_b, current_waist.input_b)
        self.assertEquals(expected_motor.pin_a, current_waist.pin_a)
        self.assertEquals(expected_motor.pin_b, current_waist.pin_b)

    def test_should_return_shoulder_motor(self):
        expected_motor = Motor(23, 24)
        shoulder = Motor(23, 24)
        arm = Arm(None, shoulder, None, None, None, None)

        current_waist = arm.get_motor("s")

        self.assertEquals(expected_motor.input_a, current_waist.input_a)
        self.assertEquals(expected_motor.input_b, current_waist.input_b)
        self.assertEquals(expected_motor.pin_a, current_waist.pin_a)
        self.assertEquals(expected_motor.pin_b, current_waist.pin_b)

    def test_should_return_elbow_motor(self):
        expected_motor = Motor(17, 27)
        elbow = Motor(17, 27)
        arm = Arm(None, None, elbow, None, None, None)

        current_waist = arm.get_motor("e")

        self.assertEquals(expected_motor.input_a, current_waist.input_a)
        self.assertEquals(expected_motor.input_b, current_waist.input_b)
        self.assertEquals(expected_motor.pin_a, current_waist.pin_a)
        self.assertEquals(expected_motor.pin_b, current_waist.pin_b)

    def test_should_return_wrist_motor(self):
        expected_motor = Motor(16, 20)
        wrist = Motor(16, 20)
        arm = Arm(None, None, None, wrist, None, None)

        current_waist = arm.get_motor("u")

        self.assertEquals(expected_motor.input_a, current_waist.input_a)
        self.assertEquals(expected_motor.input_b, current_waist.input_b)
        self.assertEquals(expected_motor.pin_a, current_waist.pin_a)
        self.assertEquals(expected_motor.pin_b, current_waist.pin_b)

    def test_should_return_gripper_motor(self):
        expected_motor = Motor(5, 6)
        gripper = Motor(5, 6)
        arm = Arm(None, None, None, None, gripper, None)

        current_waist = arm.get_motor("g")

        self.assertEquals(expected_motor.input_a, current_waist.input_a)
        self.assertEquals(expected_motor.input_b, current_waist.input_b)
        self.assertEquals(expected_motor.pin_a, current_waist.pin_a)
        self.assertEquals(expected_motor.pin_b, current_waist.pin_b)

    def test_should_return_led(self):
        expected_led = Pin(21)
        led = Pin(21)

        arm = Arm(None, None, None, None, None, led)

        current_led = arm.get_motor("l")

        self.assertEquals(expected_led.pin_value, current_led.pin_value)
        self.assertEquals(expected_led.pin_number, current_led.pin_number)

    def test_should_return_none_motor(self):
        waist = Motor(13, 19)
        arm = Arm(waist, None, None, None, None, None)
        current_waist = arm.get_motor("x")

        self.assertIsNone(current_waist)

if __name__ == '__main__':
    unittest.main()

