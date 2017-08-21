class Arm_partial:
    def __init__(self, waist, shoulder, elbow, wrist, gripper, led):
        self._led = led
        self._gripper = gripper
        self._wrist = wrist
        self._waist = waist
        self._shoulder = shoulder
        self._elbow = elbow

    @property
    def led(self):
        return self._led

    @property
    def waist(self):
        return self._waist

    @property
    def shoulder(self):
        return self._shoulder

    @property
    def elbow(self):
        return self._elbow

    @property
    def wrist(self):
        return self._wrist

    @property
    def elbow(self):
        return self._elbow

    @property
    def gripper(self):
        return self._gripper

    def get_motor(self, param):
        if param == "w":
            print "waist is selected ..."
            return self._waist

        elif param == "s":
            print "shoulder is selected ..."
            return self._shoulder

        elif param == "e":
            print "elbow is selected ..."
            return self._elbow

        elif param == "u":
            print "wrist is selected ..."
            return self._wrist

        elif param == "g":
            print "gripper is selected ..."
            return self._gripper

        elif param == "l":
            print "Led is selected .."
            return self._led

        else:
            print "no motor selected ..."
            return None
