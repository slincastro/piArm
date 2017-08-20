class Joint:
    def __init__(self, id, name, motor, encoder):
        self._id = id
        self._name = name
        self._motor = motor
        self._encoder = encoder

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def motor(self):
        return self._motor

    @property
    def encoder(self):
        return self._encoder



