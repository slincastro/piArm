import ConfigParser


class Configuration():

    def configure_test(self):
        config = ConfigParser.RawConfigParser()
        config.add_section('Constants')
        config.set('Constants', 'coefficient_conversion', '100.00')

        with open('config.cfg', 'wb') as configfile:
            config.write(configfile)
