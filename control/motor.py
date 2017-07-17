

class Motor():
    def __init__(self):
        self._inputA = False
        self._inputB = False

    @property
    def InputA(self):
        return self._inputA

    @property
    def InputB(self):
        return self._inputB

    def Left(self):
        self._inputA=True
        self._inputB=False

    def Right(self):
        self._inputB=True
        self._inputA=False
