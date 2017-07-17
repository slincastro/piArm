

class Motor():
    def __init__(self):
        self._left = False
        self._right = False

    @property
    def Left(self):
        return self._left

    @property
    def Right(self):
        return self._right

    def on(self):
        self._left=True
