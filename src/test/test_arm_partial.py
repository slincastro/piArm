import sys
import unittest

sys.path.append('../../')

from src.main.domain.motor import Motor
from src.main.domain.arm_partial import Arm_partial
from src.main.domain.pin import Pin


class TestArmPartial(unittest.TestCase):

    def test_should_return_waist(self):
        expected_motor = Motor(13, 19)
        waist = Motor(13, 19)
        arm = Arm_partial(waist, None, None, None, None, None)

        self.assertEquals(expected_motor.pin_a.number, arm.waist.pin_a.number)
        self.assertEquals(expected_motor.pin_b.number, arm.waist.pin_b.number)
        self.assertEquals(expected_motor.pin_a.value, arm.waist.pin_a.value)
        self.assertEquals(expected_motor.pin_b.value, arm.waist.pin_b.value)

    def test_should_return_waist_motor(self):
        expected_motor = Motor(13, 19)
        waist = Motor(13, 19)
        arm = Arm_partial(waist, None, None, None, None, None)

        current_waist = arm.get_motor("w")

        self.assertEquals(expected_motor.pin_a.number, current_waist.pin_a.number)
        self.assertEquals(expected_motor.pin_b.number, current_waist.pin_b.number)
        self.assertEquals(expected_motor.pin_a.value, current_waist.pin_a.value)
        self.assertEquals(expected_motor.pin_b.value, current_waist.pin_b.value)

    def test_should_return_shoulder_motor(self):
        expected_motor = Motor(23, 24)
        shoulder = Motor(23, 24)
        arm = Arm_partial(None, shoulder, None, None, None, None)

        current_waist = arm.get_motor("s")

        self.assertEquals(expected_motor.pin_a.number, current_waist.pin_a.number)
        self.assertEquals(expected_motor.pin_b.number, current_waist.pin_b.number)
        self.assertEquals(expected_motor.pin_a.value, current_waist.pin_a.value)
        self.assertEquals(expected_motor.pin_b.value, current_waist.pin_b.value)

    def test_should_return_elbow_motor(self):
        expected_motor = Motor(17, 27)
        elbow = Motor(17, 27)
        arm = Arm_partial(None, None, elbow, None, None, None)

        current_waist = arm.get_motor("e")

        self.assertEquals(expected_motor.pin_a.number, current_waist.pin_a.number)
        self.assertEquals(expected_motor.pin_b.number, current_waist.pin_b.number)
        self.assertEquals(expected_motor.pin_a.value, current_waist.pin_a.value)
        self.assertEquals(expected_motor.pin_b.value, current_waist.pin_b.value)

    def test_should_return_wrist_motor(self):
        expected_motor = Motor(16, 20)
        wrist = Motor(16, 20)
        arm = Arm_partial(None, None, None, wrist, None, None)

        current_waist = arm.get_motor("u")

        self.assertEquals(expected_motor.pin_a.number, current_waist.pin_a.number)
        self.assertEquals(expected_motor.pin_b.number, current_waist.pin_b.number)
        self.assertEquals(expected_motor.pin_a.value, current_waist.pin_a.value)
        self.assertEquals(expected_motor.pin_b.value, current_waist.pin_b.value)

    def test_should_return_gripper_motor(self):
        expected_motor = Motor(5, 6)
        gripper = Motor(5, 6)
        arm = Arm_partial(None, None, None, None, gripper, None)

        current_waist = arm.get_motor("g")

        self.assertEquals(expected_motor.pin_a.number, current_waist.pin_a.number)
        self.assertEquals(expected_motor.pin_b.number, current_waist.pin_b.number)
        self.assertEquals(expected_motor.pin_a.value, current_waist.pin_a.value)
        self.assertEquals(expected_motor.pin_b.value, current_waist.pin_b.value)

    def test_should_return_led(self):
        expected_led = Pin(21)
        led = Pin(21)

        arm = Arm_partial(None, None, None, None, None, led)

        current_led = arm.get_motor("l")

        self.assertEquals(expected_led.value, current_led.value)
        self.assertEquals(expected_led.number, current_led.number)

    def test_should_return_none_motor(self):
        waist = Motor(13, 19)
        arm = Arm_partial(waist, None, None, None, None, None)
        current_waist = arm.get_motor("x")

        self.assertIsNone(current_waist)

if __name__ == '__main__':
    unittest.main()

