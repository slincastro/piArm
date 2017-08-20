from src.main.domain.joint import Joint


class HorizontalJoint(Joint):

    def left(self):
        self.motor.turn_left()
