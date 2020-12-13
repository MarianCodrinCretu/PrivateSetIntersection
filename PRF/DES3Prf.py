from AOP.DataInterceptor import changePlaintextValidity, logCipherDetailsErrors
from PRF.PRFAbstract import PRFAbstract
from Crypto.Cipher import DES3


class DES3Prf(PRFAbstract):
    @changePlaintextValidity
    def computePrf(self, plaintext):
        result = self._cipher.encrypt(plaintext)
        return result

    def setAlgorithm(self):
        self._algorithm = DES3

    @logCipherDetailsErrors
    def setCipher(self):
        if self._mode == self._algorithm.MODE_ECB:
            self._cipher = self._algorithm.new(self._key, self._mode)
        elif self._mode == self._algorithm.MODE_CTR:
            self._cipher = self._algorithm.new(self._key, self._mode, nonce=b'')
        else:
            self._cipher = self._algorithm.new(self._key, self._mode, iv=self._iv)