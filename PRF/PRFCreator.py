from abc import ABC

from PRF.AESPrf import AESPrf
from PRF.DES3Prf import DES3Prf
from PRF.DESPrf import DESPrf
from Shared.Enums.PrfScopeEnum import PrfScopeEnum
from Shared.Enums.PrfTypeEnum import PrfTypeEnum


class PRFCreator(ABC):
    def __init__(self, prfType, key, iv=b''):
        self._iv = iv
        self._key = key
        self.createPrf(prfType)

    def createPrf(self, prfType):
        if prfType == PrfTypeEnum.DES:
            self._prf = DESPrf(self._key, self._iv)
        elif prfType == PrfTypeEnum.AES:
            self._prf = AESPrf(self._key, self._iv)
        elif prfType == PrfTypeEnum.DES3:
            self._prf = DES3Prf(self._key, self._iv)

    def computePrf(self, plaintext, scope=PrfScopeEnum.GENERIC):
        return self._prf.computePrf(plaintext, scope)

