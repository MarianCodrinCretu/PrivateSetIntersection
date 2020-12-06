from abc import ABC
from AOP.DataInterceptor import logCipherDetailsErrors
from PRF.PrfScopeEnum import PrfScopeEnum


class PRFAbstract(ABC):
    def __init__(self, iv, key, scope):
        self._iv = iv
        self._key = key
        self._scope = scope
        self.setAlgorithm()
        self._mode = self._algorithm.MODE_CBC
        self.setMode()
        self.setCipher()


    def setAlgorithm(self):
        raise NotImplementedError()

    def getAlgorithm(self):
        return self._algorithm

    def computePrf(self, plaintext):
        raise NotImplementedError()

    def setMode(self):
        if self._scope == PrfScopeEnum.PRG:
            self._mode = self._algorithm.MODE_CTR
        elif self._scope == PrfScopeEnum.GENERATOR:
            self._mode = self._algorithm.MODE_ECB

    @logCipherDetailsErrors
    def setCipher(self):
        if self._mode == self._algorithm.MODE_ECB or self._mode == self._algorithm.MODE_CTR:
            self._cipher = self._algorithm.new(self._key, self._mode)
        else:
            self._cipher = self._algorithm.new(self._key, self._mode, iv=self._iv)


