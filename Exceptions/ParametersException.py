class ParametersException(Exception):

    def __init__(self, arg):
        self.message = '[[[ERROR]]] ParametersException occurred: '+arg
        super().__init__(self.message)

    def __str__(self):
        return self.message