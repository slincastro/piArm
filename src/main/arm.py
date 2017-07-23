

class Arm:

    def __init__(self, waist):
        self._waist = waist

    @property
    def waist(self):
        return self._waist

    def get_motor(self, param):
        if param == "w":
            print "waist is selected ..."
            return self._waist
        else:
            print "no motor selected ..."
            return None

