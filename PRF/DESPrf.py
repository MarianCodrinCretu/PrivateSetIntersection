from PRF.PRFAbstract import PRFAbstract
from Crypto.Cipher import DES


class DESPrf(PRFAbstract):
    def setAlgorithm(self):
        self._algorithm = DES
