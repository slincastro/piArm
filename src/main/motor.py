

class Motor:
    def __init__(self):
        self._inputA = False
        self._inputB = False

    @property
    def input_a(self):
        return self._inputA

    @property
    def input_b(self):
        return self._inputB

    def left(self):
        self._inputA = True
        self._inputB = False

    def right(self):
        self._inputB = True
        self._inputA = False

    def stop(self):
        self._inputA = False
        self._inputB = False

