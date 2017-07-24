
class Pin:

    def __init__(self, pin):
        self._pin = int(pin)
        self._value = False

    @property
    def pin_number(self):
        return self._pin

    @property
    def pin_value(self):
        return self._value

    def on(self):
        self._value = True

    def off(self):
        self._value = False
