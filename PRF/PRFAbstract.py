from abc import ABC

from AOP.DataInterceptor import logCipherDetailsErrors, changePlaintextValidity
from PRF.PrfScopeEnum import PrfScopeEnum


class PRFAbstract(ABC):
    def __init__(self, iv, key):
        self._iv = iv
        self._key = key
        self.setAlgorithm()
        self.setEncryptionAlgorithms()

    def setAlgorithm(self):
        pass

    def getAlgorithm(self):
        if self._algorithm is not None:
            return self._algorithm

    @changePlaintextValidity
    def computePrf(self, plaintext, scope):
        return self._modesScopeDictionary[scope].encrypt(plaintext)

    @logCipherDetailsErrors
    def setEncryptionAlgorithms(self):
        self._modesScopeDictionary = {
            PrfScopeEnum.PRG: self._algorithm.new(self._key, self._algorithm.MODE_CTR, nonce=b''),
            PrfScopeEnum.GENERATOR: self._algorithm.new(self._key, self._algorithm.MODE_ECB),
            PrfScopeEnum.GENERIC: self._algorithm.new(self._key, self._algorithm.MODE_CBC)
        }
