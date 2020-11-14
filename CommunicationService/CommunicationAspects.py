import aspectlib
from Crypto.Cipher import AES

class CommunicationAspects:

    @aspectlib.Aspect
    def encryptDataAES(self, aesKey, aesIV):
        cipher = AES.new(aesKey, AES.MODE_CBC, aesIV)
        data = yield aspectlib.Proceed
        yield aspectlib.Return(cipher.encrypt(data))