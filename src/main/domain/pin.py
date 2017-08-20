
class Pin:

    def __init__(self, pin):
        self._pin = int(pin)
        self._value = False

    @property
    def number(self):
        return self._pin

    @property
    def value(self):
        return self._value

    def on(self):
        self._value = True

    def off(self):
        self._value = False

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
