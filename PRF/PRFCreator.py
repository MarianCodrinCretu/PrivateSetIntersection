from abc import ABC, abstractmethod


class PRFCreator(ABC):
    def __init__(self, iv, key) -> None:
        self._iv = iv
        self._key = key
        self._prf = self.createPrf()

    @abstractmethod
    def createPrf(self):
        pass

    def computePrf(self, plaintext, scope):
        return self._prf.computePrf(plaintext, scope)

    # @staticmethod
    # def getPrfInstance(prfType, key, iv=b''):
    #     if prfType == 'DES':
    #         return DESPrfCreator(iv, key)
    #     elif prfType == 'AES':
    #         return AESPrfCreator(iv, key)
    #     elif prfType == 'DES3':
    #         return DES3PrfCreator(iv, key)

