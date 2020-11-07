import math
from unittest import TestCase

from Exceptions.InvalidColumnNamesException import InvalidColumnNamesException
from DataEngineeringService.XLSParser import XLSParser


class XLSParserShould(TestCase):

    xlsFile = 'testXLS.xlsx'
    xlsFileExtraColumn = 'testXLSExtraColumn.xlsx'
    xlsFileExtraData = 'testXLSExtraData.xlsx'

    def test_getColumnNamesWhenNormallyFormat(self):

        xlsParser =XLSParser()
        columnsList = xlsParser.extractColumnsNames(self.xlsFile)
        self.assertListEqual(columnsList, ['ID', 'Name', 'Address'])

    def test_getDataWhenNormallyForm(self):

        xlsParser = XLSParser()
        data = xlsParser.parse(self.xlsFile)
        result = {'ID' : [1, 2, 3, 4], 'Name':['Andrada ', 'Stefania', 'Andrei', 'Marian'], 'Address': ['California', 'New Jersey', 'Princeton', 'New York']}
        self.assertDictEqual(data, result)

    def test_getColumnNamesWhenExistsExtraColumnWithNoData(self):
        xlsParser = XLSParser()
        columnsList = xlsParser.extractColumnsNames(self.xlsFileExtraColumn)
        self.assertListEqual(columnsList, ['ID', 'Name', 'Address', 'Telephone'])

    def test_getDataWhenExistsExtraColumnWithNoData(self):
        xlsParser = XLSParser()
        data = xlsParser.parse(self.xlsFileExtraColumn)
        result = {'ID': [1, 2, 3, 4], 'Name': ['Andrada ', 'Stefania', 'Andrei', 'Marian'],
                  'Address': ['California', 'New Jersey', 'Princeton', 'New York'], 'Telephone':[math.nan, math.nan, math.nan, math.nan]}
        self.assertListEqual(data['ID'], result['ID'])
        self.assertListEqual(data['Name'], result['Name'])
        self.assertListEqual(data['Address'], result['Address'])
        counter = 0
        for element in data['Telephone']:
            self.assertTrue(math.isnan(element))
            counter+=1
        self.assertEqual(counter,4)

    def test_getColumnNamesWhenExistsExtraData(self):
        xlsParser = XLSParser()
        with self.assertRaises(InvalidColumnNamesException):
            columnsList = xlsParser.extractColumnsNames(self.xlsFileExtraData)

    def test_getDataWhenExistsExtraData(self):
        xlsParser = XLSParser()
        with self.assertRaises(InvalidColumnNamesException):
            data = xlsParser.parse(self.xlsFileExtraData)


