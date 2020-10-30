from DataEngineeringService.CSVParser import CSVParser
from DataEngineeringService.DataEngineering import DataEngineering
from DataEngineeringService.XLSParser import XLSParser

dataEngineering = DataEngineering(CSVParser(), XLSParser())

print(dataEngineering.parse("C:\\Users\\1\\Desktop\\PSI\\demo.xlsx"))