from abc import ABC

from AOP.DataInterceptor import logCipherDetailsErrors, changePlaintextValidity
from Shared.Enums.PrfScopeEnum import PrfScopeEnum


class PRFAbstract(ABC):
    def __init__(self, key, iv=b''):
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
            PrfScopeEnum.PRG: self.getAlgorithm().new(self._key, self.getAlgorithm().MODE_CTR, nonce=b''),
            PrfScopeEnum.GENERATOR: self.getAlgorithm().new(self._key, self.getAlgorithm().MODE_ECB),
            PrfScopeEnum.GENERIC: self.getAlgorithm().new(self._key, self.getAlgorithm().MODE_CFB)
        }

