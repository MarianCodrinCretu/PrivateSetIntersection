from Exceptions.InvalidColumnNamesException import InvalidColumnNamesException
from DataEngineeringService.Parser import Parser
import csv

# CSV parser class
# author mcretu

class CSVParser(Parser):

    def extractColumnNames(self, file):

        with open(file, 'r', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            columnNames = next(spamreader)

            for name in columnNames:
                if not name.replace(" ", "").isalpha():
                    raise InvalidColumnNamesException("Column names are not alphabetic")

            return columnNames

    def parse(self, file):

        columnNames = self.extractColumnNames(file)

        columns = {}

        with open(file, 'r') as csvfile:
            spamreader = csv.reader(csvfile)

            row = next(spamreader)

            try:
                while (row is not None):
                    row = next(spamreader)
                    for feature in range(len(row)):
                        if columnNames[feature] not in columns:
                            columns[columnNames[feature]] = [row[feature]]
                        else:
                            columns[columnNames[feature]].append(row[feature])
            except StopIteration:
                pass

        return columns
