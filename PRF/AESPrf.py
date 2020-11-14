from AOP.DataInterceptor import changePlaintextValidity
from PRF.PRFAbstract import PRFAbstract
from Crypto.Cipher import AES


class AESPrf(PRFAbstract):

    @changePlaintextValidity
    def computePrf(self, plaintext):
        result = self._cipher.encrypt(plaintext)
        print('PRF with AES', result)
        return result

    def setAlgorithm(self):
        self._algorithm = AES

    # def setCipher(self):
    #     self._cipher = AES.new(self._key, iv=self._iv)
