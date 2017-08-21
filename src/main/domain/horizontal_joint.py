from src.main.domain.joint import Joint


class HorizontalJoint(Joint):
    def left(self):
        if self.encoder >= 150:
            self.motor.stop()
        else:
            self.motor.turn_left()

    def right(self):
        if self.encoder >= 150:
            self.motor.stop()
        else:
            self.motor.turn_right()


