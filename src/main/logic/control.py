import sys
sys.path.append('../../')
from src.main.logic.converter import Converter


class Control:

    def __init__(self, motor, executor):
        self._motor = motor
        self._executor = executor

    def turn_left(self, degrees):
        self._motor.left()
        print "move left " + str(degrees) + " degrees"
        converter = Converter()
        seconds = converter.to_seconds(degrees)
        self._executor.move(self._motor, seconds)
        self._motor.stop()
        self._executor.stop(self._motor)

    def turn_right(self, degrees):
        self._motor.right()
        print "move right " + str(degrees) + " degrees"
        converter = Converter()
        seconds = converter.to_seconds(degrees)
        self._executor.move(self._motor, seconds)
        self._motor.stop()
        self._executor.stop(self._motor)
        pass

