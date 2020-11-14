import pickle
import time

import aspectlib
from Crypto.Cipher import AES
from CommunicationService.Communication import Communication
from Constants import SNOOZE_FACTOR


class ComSend(Communication):

    @aspectlib.Aspect
    def encryptDataAES(self, toBeSent, flag):

        if flag=='NoAES':
            yield aspectlib.Proceed
        else:
            cipher = AES.new(self.aesKey, AES.MODE_CFB, self.aesIV)
            data = yield aspectlib.Proceed
            yield aspectlib.Return(cipher.encrypt(data))

    @aspectlib.Aspect
    def snoozeAdaptivelyTime(self, data):
        yield time.sleep(SNOOZE_FACTOR * len(data))

    def snoozeTime(self, data):
        time.sleep(0.2)


    def processData(self, toBeSent, flag):
        binaryDict = pickle.dumps(toBeSent)
        return binaryDict


    def send(self, toBeSent, ipDestination, portDestination, HEADERSIZE, flag=None):

        with aspectlib.weave(self.processData, self.encryptDataAES):
            binaryDict = self.processData(toBeSent, flag)

        socket = self._socketPool.acquire()
        socket.connect((ipDestination, portDestination))

        binaryDict = bytes(f"{len(binaryDict):<{HEADERSIZE}}", 'utf-8') + binaryDict
        socket.send(binaryDict)
        self._socketPool.release(socket)

        with aspectlib.weave(self.snoozeTime, self.snoozeAdaptivelyTime):
            self.snoozeTime(binaryDict)
