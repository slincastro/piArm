import sys
sys.path.append('../../')
from src.main.Infra.executor import Executor


class Control:

    def __init__(self, motor, executor):
        self._motor = motor
        self._executor = executor

    def turn_left(self, degrees):
        self._motor.left()
        self._executor.move(self._motor, degrees)
        self._motor.stop()

