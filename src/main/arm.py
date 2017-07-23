

class Arm:

    def __init__(self, waist):
        self._waist = waist

    @property
    def waist(self):
        return self._waist

    def get_motor(self, param):
        return self._waist


