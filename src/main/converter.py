import ConfigParser


class Converter:

    def __init__(self):
        config = ConfigParser.RawConfigParser()
        config.read('config.cfg')
        self._coefficient_conversion = config.getfloat('Constants', 'coefficient_conversion')

    def to_seconds(self, degrees):
        coefficient_conversion = self._coefficient_conversion
        return degrees / coefficient_conversion
