# InvalidFileExtensionException -- raised when invalid format of the file

# author mcretu
# cretu.marian.5000@gmail.com

class InvalidFileExtensionException(Exception):

    def __init__(self, arg):
        self.args = arg
        super().__init__(self.args)

