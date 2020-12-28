class PsiException(Exception):

    def __init__(self, arg):
        self.args = '[[[ERROR]]] PsiException occurred: '+arg