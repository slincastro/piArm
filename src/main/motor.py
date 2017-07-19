

class Motor:
    def __init__(self, pin_a, pin_b):
        self._inputA = False
        self._inputB = False
        self._pinA = pin_a
        self._pinB = pin_b

    @property
    def input_a(self):
        return self._inputA

    @property
    def input_b(self):
        return self._inputB

    @property
    def pin_a(self):
        return self._pinA

    @property
    def pin_b(self):
        return self._pinB

    def left(self):
        self._inputA = True
        self._inputB = False

    def right(self):
        self._inputB = True
        self._inputA = False

    def stop(self):
        self._inputA = False
        self._inputB = False





