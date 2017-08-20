

class Joint_partial:

    def __init__(self, name, direction, value):
        self._name = name
        self._direction = direction
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def direction(self):
        return self._direction

    @property
    def value(self):
        return self._value

