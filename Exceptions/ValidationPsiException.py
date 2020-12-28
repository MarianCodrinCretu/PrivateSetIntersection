class ValidationPsiException(Exception):

    def __init__(self, arg):
        self.args = '[[[ERROR]]] ValidationPsiException occurred: '+arg