class ParametersException(Exception):

    def __init__(self, arg):
        self.args = '[[[ERROR]]] ParametersException occurred: '+arg