import math
from unittest import TestCase

from DataEngineeringService.CSVParser import CSVParser
from Exceptions.InvalidColumnNamesException import InvalidColumnNamesException


class CSVParserShould(TestCase):

    csvFile = 'testCSV.csv'
    csvFileExtraColumn = 'testCSVExtraColumn.csv'
    csvFileExtraData = 'testCSVExtraData.csv'

    def test_getColumnNamesWhenNormallyFormat(self):

        csvParser =CSVParser()
        columnsList = csvParser.extractColumnsNames(self.csvFile)
        self.assertListEqual(columnsList, ['ID', 'Name', 'Address'])

    def test_getDataWhenNormallyForm(self):
        csvParser = CSVParser()
        data = csvParser.parse(self.csvFile)
        result = {'ID' : ['1', '2', '3', '4'], 'Name':['Andrada ', 'Stefania', 'Andrei', 'Marian'], 'Address': ['California', 'New Jersey', 'Princeton', 'New York']}
        self.assertDictEqual(data, result)

    def test_getColumnNamesWhenExistsExtraColumnWithNoData(self):
        csvParser = CSVParser()
        columnsList = csvParser.extractColumnsNames(self.csvFileExtraColumn)
        self.assertListEqual(columnsList, ['ID', 'Name', 'Address', 'Telephone'])

    def test_getDataWhenExistsExtraColumnWithNoData(self):
        csvParser = CSVParser()
        data = csvParser.parse(self.csvFileExtraColumn)
        result = {'ID': ['1', '2', '3', '4'], 'Name': ['Andrada ', 'Stefania', 'Andrei', 'Marian'],
                  'Address': ['California', 'New Jersey', 'Princeton', 'New York'], 'Telephone':[math.nan, math.nan, math.nan, math.nan]}
        self.assertListEqual(data['ID'], result['ID'])
        self.assertListEqual(data['Name'], result['Name'])
        self.assertListEqual(data['Address'], result['Address'])
        counter = 0
        print(data)
        for element in data['Telephone']:
            self.assertTrue(element=='')
            counter+=1
        self.assertEqual(counter,4)

    def test_getColumnNamesWhenExistsExtraData(self):
        csvParser = CSVParser()
        with self.assertRaises(InvalidColumnNamesException):
            columnsList = csvParser.extractColumnsNames(self.csvFileExtraData)

    def test_getDataWhenExistsExtraData(self):
        csvParser = CSVParser()
        with self.assertRaises(InvalidColumnNamesException):
            data = csvParser.parse(self.csvFileExtraData)
