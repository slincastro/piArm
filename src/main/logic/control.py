import sys
sys.path.append('../../')
from src.main.logic.converter import Converter
import time


class Control:

    def __init__(self, motor, executor):
        self._motor = motor
        self._executor = executor

    def turn_left(self, degrees):
        print "move left " + str(degrees) + " degrees"

        self._motor.left()
        self.go_move(degrees)

    def turn_right(self, degrees):
        print "move right " + str(degrees) + " degrees"

        self._motor.right()
        self.go_move(degrees)

    def go_move(self, degrees):
        converter = Converter()
        seconds = converter.to_seconds(degrees)
        self._executor.move(self._motor)
        time.sleep(seconds)
        self._motor.stop()
        self._executor.move(self._motor)

