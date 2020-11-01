import Entity


class RandomUtils:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if RandomUtils.__instance is None:
            RandomUtils()
        return RandomUtils.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if RandomUtils.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            RandomUtils.__instance = self

    @staticmethod
    def generateSSender(w: int):
        pass

    @staticmethod
    def initMatrixDReceiver(m: int, w: int):
        pass

    @staticmethod
    def initMatrixAReceiver(m: int, w: int):
        pass

    @staticmethod
    def generateKey():
        pass


class PSIAlgoUtils:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if PSIAlgoUtils.__instance is None:
            PSIAlgoUtils()
        return PSIAlgoUtils.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if PSIAlgoUtils.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            PSIAlgoUtils.__instance = self

    @staticmethod
    def computeBReceiver(D: list, A: list):
        pass

    @staticmethod
    def operateDReceiver(D: list):
        pass

