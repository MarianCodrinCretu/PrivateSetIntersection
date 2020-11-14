import pickle
import aspectlib
from Crypto.Cipher import AES
from CommunicationService.Communication import Communication


class ComSend(Communication):

    @aspectlib.Aspect
    def encryptDataAES(self, toBeSent):

        cipher = AES.new(self.aesKey, AES.MODE_CFB, self.aesIV)
        data = yield aspectlib.Proceed
        yield aspectlib.Return(cipher.encrypt(data))


    def processData(self, toBeSent):
        binaryDict = pickle.dumps(toBeSent)
        return binaryDict


    def send(self, toBeSent, ipDestination, portDestination, HEADERSIZE):

        with aspectlib.weave(self.processData, self.encryptDataAES):
            binaryDict = self.processData(toBeSent)

        socket = self._socketPool.acquire()
        socket.connect((ipDestination, portDestination))

        binaryDict = bytes(f"{len(binaryDict):<{HEADERSIZE}}", 'utf-8') + binaryDict
        socket.send(binaryDict)
        self._socketPool.release(socket)
