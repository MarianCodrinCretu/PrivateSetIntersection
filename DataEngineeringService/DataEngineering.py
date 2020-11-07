from DataEngineeringService import CSVParser, XLSParser
from Exceptions.InvalidFileExtensionException import InvalidFileExtensionException

# DataEngineeringService class for processing received data from input

# author mcretu
# cretu.marian.5000@gmail.com


class DataEngineering():

    def __init__ (self, csvParser : CSVParser, xlsParser: XLSParser):
        self.__csvParser = csvParser
        self.__xlsParser = xlsParser



    # public method for getting column names

       # private method for checking file extension is properly
    def __checkExtension(self, file):

        if '.' not in file:
            raise InvalidFileExtensionException("The file has no format!" +
                                                "Please use xlsx or csv format")
        extension = file.split(".")[1]
        print(extension)
        if extension not in ("xlsx", "csv"):
            raise InvalidFileExtensionException("Format of the file is not recognized! \n" +
                                                "Please use xlsx or csv format")
        return extension

    def extractColumnNames(self, file):

        extension = self.__checkExtension(file)
        columnNames = []
        if extension == "xlsx":
            columnNames = self.__xlsParser.extractColumnsNames(file)
            print(columnNames)
        elif extension == "csv":
            columnNames = self.__csvParser.extractColumnsNames(file)
            print(columnNames)

        return columnNames

    def parse(self, file):

        extension = self.__checkExtension(file)

        data = []
        if extension == "xlsx":
            data = self.__xlsParser.parse(file)
        elif extension == "csv":
            data = self.__csvParser.parse(file)

        for element in data:
            data[element] = [str(x) for x in data[element]]

        return data




