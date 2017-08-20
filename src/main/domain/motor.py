import sys
sys.path.append('../../')

from src.main.domain.pin import Pin


class Motor:
    def __init__(self, pin_a, pin_b):
        self._pin_a = Pin(pin_a)
        self._pin_b = Pin(pin_b)
        self._is_on = False

    @property
    def pin_a(self):
        return self._pin_a

    @property
    def pin_b(self):
        return self._pin_b

    def turn_left(self):
        self._is_on = True
        self.pin_a.on()
        self.pin_b.off()

    def turn_right(self):
        self._is_on = True
        self.pin_a.off()
        self.pin_b.on()

    def stop(self):
        self.pin_a.off()
        self.pin_b.off()
        self._is_on = False

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def is_on(self):
        return self._is_on
