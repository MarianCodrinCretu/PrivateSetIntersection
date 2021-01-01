# InvalidColumnNamesException -- raised when invalid names of columns (alphabetic)

# author mcretu
# cretu.marian.5000@gmail.com

class InvalidColumnNamesException(Exception):

    def __init__(self, arg):
        self.args = arg
        super().__init__(self.args)

