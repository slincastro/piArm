
class Control:
    def __init__(self, motor):
        self._motor = motor

    def turn_left(self, degrees):
        self._motor.left()
