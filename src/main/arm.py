

class Arm:

    def __init__(self, waist, shoulder):
        self._waist = waist
        self._shoulder = shoulder

    @property
    def waist(self):
        return self._waist

    @property
    def shoulder(self):
        return self._shoulder

    def get_motor(self, param):
        if param == "w":
            print "waist is selected ..."
            return self._waist
        elif param == "s":
            print "shoulder is selected ..."
            return self._shoulder
        else:
            print "no motor selected ..."
            return None

