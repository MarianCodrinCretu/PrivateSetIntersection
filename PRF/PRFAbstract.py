from abc import ABC
from AOP.DataInterceptor import logCipherDetailsErrors


class PRFAbstract(ABC):
    def __init__(self, iv, key):
        self._iv = iv
        self._key = key
        self.setAlgorithm()
        self.setCipher()

    def setAlgorithm(self):
        raise NotImplementedError()

    def getAlgorithm(self):
        return self._algorithm

    def computePrf(self, plaintext):
        raise NotImplementedError()

    @logCipherDetailsErrors
    def setCipher(self):
        self._cipher = self._algorithm.new(self._key, self._algorithm.MODE_CBC, iv=self._iv)


