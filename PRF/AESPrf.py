from PRF.PRFAbstract import PRFAbstract
from Crypto.Cipher import AES

class AESPrf(PRFAbstract):
    def computePrf(self, plaintext):
        result = self._cipher.encrypt(plaintext)
        print('PRF with AES', result)
        return result

    def setCipher(self):
        self._mode = AES.MODE_CBC
        if not self._iv:
            self._cipher = AES.new(self._key, self._mode)
        else:
            self._cipher = AES.new(self._key, self._mode, iv = self._iv)

