import sys
sys.path.append('../../')

from src.main.domain.pin import Pin


class Motor:
    def __init__(self, pin_a, pin_b):
        self._pin_a = Pin(pin_a)
        self._pin_b = Pin(pin_b)

    @property
    def pin_a(self):
        return self._pin_a

    @property
    def pin_b(self):
        return self._pin_b

    def turn_left(self):
        self.pin_a.on()
        self.pin_b.off()

    def turn_right(self):
        self.pin_a.off()
        self.pin_b.on()

    def stop(self):
        self.pin_a.off()
        self.pin_b.off()
