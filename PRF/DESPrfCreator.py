from PRF.DESPrf import DESPrf
from PRF.PRFCreator import PRFCreator


class DESPrfCreator(PRFCreator):
    def createPrf(self):
        return DESPrf(self._iv, self._key, self._scope)
