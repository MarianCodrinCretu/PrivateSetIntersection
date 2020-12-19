from PRF.PRFAbstract import PRFAbstract
from Crypto.Cipher import AES


class AESPrf(PRFAbstract):
    def setAlgorithm(self):
        self._algorithm = AES

