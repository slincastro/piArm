class Arm:
    def __init__(self, waist, shoulder):
        self._shoulder = shoulder
        self._waist = waist

    @property
    def waist(self):
        return self._waist

    @property
    def shoulder(self):
        return self._shoulder
