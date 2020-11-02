from PRF.PRFAbstract import PRFAbstract
from Crypto.Cipher import DES

class DESPrf(PRFAbstract):
    def computePrf(self, plaintext):
        return self._cipher.encrypt(plaintext)

    def setCipher(self):
        self._mode = DES.MODE_CBC
        if not self._iv:
            self._cipher = DES.new(self._key, self._mode)
        else:
            self._cipher = DES.new(self._key, self._mode, iv=self._iv)
