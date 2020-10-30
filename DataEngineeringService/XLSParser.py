import pandas as pd
#run pip install xlrd
from Exceptions.InvalidColumnNamesException import InvalidColumnNamesException
from DataEngineeringService.Parser import Parser

# XLS parser class
# author mcretu

class XLSParser(Parser):

    def extractColumnsNames(self, file):
        columnNames = list(pd.read_excel(file))
        for name in columnNames:
            if not name.replace(" ", "").isalpha():
                raise InvalidColumnNamesException("Column names are not alphabetic")

        return columnNames

    def parse(self, file):

        columnNames = self.extractColumnsNames(file)
        df = pd.read_excel(file)
        columns={}
        for columnName in columnNames:
            columns[columnName]=list(df[columnName])

        return columns