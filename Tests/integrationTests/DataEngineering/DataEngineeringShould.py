from unittest import TestCase

from DataEngineeringService.CSVParser import CSVParser
from DataEngineeringService.DataEngineering import DataEngineering
from DataEngineeringService.XLSParser import XLSParser
from Exceptions.InvalidFileExtensionException import InvalidFileExtensionException


class DataEngineeringShould(TestCase):

    dataEngineering = DataEngineering(CSVParser(), XLSParser())
    wrongExtensionFile = 'dummy.txt'
    csvFile = "testCSV.csv"
    xlsFile = "testXLS.xlsx"

    def test_failGetColumnsWhenInvalidExtension(self):
        with self.assertRaises(InvalidFileExtensionException):
            self.dataEngineering.extractColumnNames(self.wrongExtensionFile)

    def test_failParseWhenInvalidExtension(self):
        with self.assertRaises(InvalidFileExtensionException):
            self.dataEngineering.parse(self.wrongExtensionFile)

    def test_getColumnsProperlyForCSVFile(self):
        columns = self.dataEngineering.extractColumnNames(self.csvFile)
        self.assertListEqual(columns, ['ID', 'Name', 'Address'])

    def test_getColumnsProperlyForXLSFile(self):
        columns = self.dataEngineering.extractColumnNames(self.xlsFile)
        self.assertListEqual(columns, ['ID', 'Name', 'Address'])

    def test_getDataProperlyForCSVFile(self):
        data = self.dataEngineering.parse(self.csvFile)
        result = {'ID': ['1', '2', '3', '4'], 'Name': ['Andrada ', 'Stefania', 'Andrei', 'Marian'],
                  'Address': ['California', 'New Jersey', 'Princeton', 'New York']}
        self.assertDictEqual(data, result)

    def test_getDataProperlyForXLSFile(self):
        data = self.dataEngineering.parse(self.xlsFile)
        result = {'ID': ['1', '2', '3', '4'], 'Name': ['Andrada ', 'Stefania', 'Andrei', 'Marian'],
                  'Address': ['California', 'New Jersey', 'Princeton', 'New York']}
        self.assertDictEqual(data, result)





