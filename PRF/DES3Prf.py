from PRF.PRFAbstract import PRFAbstract
from Crypto.Cipher import DES3


class DES3Prf(PRFAbstract):
    def setAlgorithm(self):
        self._algorithm = DES3
