from PRF.PRFAbstract import PRFAbstract
from Crypto.Cipher import DES


class DESPrf(PRFAbstract):
    def computePrf(self, plaintext):
        # result = self._cipher.encrypt(plaintext)
        # print('PRF with DES', result)
        # return result
        pass

    def setCipher(self):
        self._mode = DES.MODE_CBC
        if not self._iv:
            self._cipher = DES.new(self._key, self._mode)
        else:
            self._cipher = DES.new(self._key, self._mode, iv=self._iv)
