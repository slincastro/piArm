from src.main.domain.joint import Joint


class VerticalJoint(Joint):
    def up(self):
        if self.encoder >= 150:
            self.motor.stop()
        else:
            self.motor.turn_left()

    def down(self):
        if self.encoder >= 150:
            self.motor.stop()
        else:
            self.motor.turn_right()