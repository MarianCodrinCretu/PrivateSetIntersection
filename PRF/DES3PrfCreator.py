from PRF.DES3Prf import DES3Prf
from PRF.PRFCreator import PRFCreator


class DES3PrfCreator(PRFCreator):
    def createPrf(self):
        return DES3Prf(self._iv, self._key, self._scope)

