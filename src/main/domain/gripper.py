class Gripper:
    def __init__(self, motor):
        self._has_gripped = False
        self._motor = motor

    @property
    def motor(self):
        return self._motor

    def has_gripped(self):
        return self._has_gripped

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def close(self):
        self.motor.turn_left()

    def open(self):
        self.motor.turn_right()

    def gripped(self):
        self.motor.stop()
        self._has_gripped = True
