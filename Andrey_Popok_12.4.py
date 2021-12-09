import logging
import random

FORMAT = '%(levelname)s - %(message)s'

class BatterySimulation():
    def __init__(self,logger):
        self.logger = logger
    
    def simulate_last_hour(self):
        for minute in range(1,60 +1):
            temperature = random.randint(20,80)
            if temperature < 30:
                self.logger.debug('{0} C'.format(temperature))
            elif temperature >=30 and temperature <=50:
                self.logger.warning('{0} C'.format(temperature))
            elif temperature >50:
                self.logger.critical('{0} C'.format(temperature))
            else:
                raise Exception('Temperature is out of range.')

logger = logging.getLogger('battery.temperature')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('battery_temperature.log',mode ='w')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)

battery_simulation = BatterySimulation(logger)
battery_simulation.simulate_last_hour()
