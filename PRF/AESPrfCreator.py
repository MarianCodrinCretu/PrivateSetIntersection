from PRF.AESPrf import AESPrf
from PRF.PRFCreator import PRFCreator


class AESPrfCreator(PRFCreator):
    def createPrf(self):
        return AESPrf(self._iv, self._key)
