from AOP.DataInterceptor import changePlaintextValidity
from PRF.PRFAbstract import PRFAbstract
from Crypto.Cipher import AES


class AESPrf(PRFAbstract):

    @changePlaintextValidity
    def computePrf(self, plaintext):
        result = self._cipher.encrypt(plaintext)
        return result

    def setAlgorithm(self):
        self._algorithm = AES

