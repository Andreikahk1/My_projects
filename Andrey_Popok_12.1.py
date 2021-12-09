import xml.etree.ElementTree as ET

class TemperatureConverter:
    def converter_celsium_to_fahrenheit(self,temperature_in_celsium):
        return 9.0/5.0 * temperature_in_celsium + 32

class ForecastXm1Parser:
    def __init__(self,temperature_converter):
        self.temperature_converter = temperature_converter

    def parse (self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root:
            day = child.find('day').text
            temperature_in_celsium = int(child.find('temperature_in_celsium').text)
            temperature_in_fahrenheit = round(self.temperature_converter.converter_celsium_to_fahrenheit(temperature_in_celsium),1)
            print('{0}: {1} Celsium, {2} Fahrenheit'.format(day,temperature_in_celsium,temperature_in_fahrenheit))

temperature_converter =  TemperatureConverter()
forecast_xml_parser = ForecastXm1Parser(temperature_converter)
forecast_xml_parser.parse('forecast.xml')
