import Entity
from Crypto.Random import random
# import random
from AOP_specifications import logMatricesBitsErrors, logNotReturnedBitsErrors


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
    @logNotReturnedBitsErrors
    def generateSSender(w: int):
        return bin(random.getrandbits(w))[2:].zfill(w)

    @staticmethod
    @logNotReturnedBitsErrors
    def initMatrixDReceiver(m: int, w: int):
        return [[1 for c in range(w)] for l in range(m)]

    @staticmethod
    @logNotReturnedBitsErrors
    def initMatrixAReceiver(m: int, w: int):
        return [[random.randint(0, 1) for c in range(w)] for l in range(m)]

    @staticmethod
    @logNotReturnedBitsErrors
    def generateKey(lambda_: int):
        return bin(random.getrandbits(lambda_))[2:].zfill(lambda_)


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
    @logMatricesBitsErrors
    def computeBReceiver(D: list, A: list):
        if len(A) != len(D):
            raise Exception("A and D should have same number of lines")
        B = []
        for l in range(len(A)):
            if len(A[l]) != len(D[l]):
                raise Exception("A and D should have same number of columns")
            v = []
            for c in range(len(A[l])):
                v.append(int(bool(A[l][c]) ^ bool(D[l][c])))
            B.append(v)
        return B

    @staticmethod
    @logMatricesBitsErrors
    def operateDReceiver(D: list):
        pass


if __name__ == "__main__":
    print(PSIAlgoUtils.computeBReceiver([[1, 0], [0, 1]], [[1, 0], [0, 1]]))
    print(RandomUtils.generateKey(3))
    # PSIAlgoUtils.operateDReceiver([[1, 0], [0, 0]])
    # print(RandomUtils.generateSSender(3))
    print(bin(random.getrandbits(5)))
