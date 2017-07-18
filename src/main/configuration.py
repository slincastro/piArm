import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('Constants')
config.set('Constants', 'coefficient_conversion', '100')

with open('config.cfg', 'wb') as configfile:
    config.write(configfile)
