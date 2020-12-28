class PrecomputationOTException(Exception):

    def __init__(self, arg):
        self.args = '[[[ERROR]]] PrecomputationOTException occurred: '+arg