from unittest import TestCase

import pandas as pd
from mockito import when, verify, unstub
from mockito.matchers import any

from DataEngineeringService.XLSParser import XLSParser
from Exceptions.InvalidColumnNamesException import InvalidColumnNamesException


class XLSParserShould(TestCase):
    xlsParser = XLSParser()

    def test_extractCorrectlyColumnNames(self):
        # setup
        file = 'fileName.xls'
        result = ['A1', 'B2', 'C3']
        when(pd).read_excel(any(str)).thenReturn(result)

        # execute
        actualResult = self.xlsParser.extractColumnsNames(file)

        # verify
        self.assertEqual(actualResult, result)
        verify(pd).read_excel(file)

        unstub()

    def test_raiseExceptionWhenNameNotProperly(self):
        # setup
        file = 'fileName.xls'
        result = ['A1..', 'B2', 'C3']
        when(pd).read_excel(any(str)).thenReturn(result)
        exception = InvalidColumnNamesException("Column names are not alphabetic")

        # execute
        with self.assertRaises(InvalidColumnNamesException) as context:
            self.xlsParser.extractColumnsNames(file)

            self.assertEqual(str(exception), context.exception)

        # verify
        verify(pd).read_excel(file)
        unstub()
