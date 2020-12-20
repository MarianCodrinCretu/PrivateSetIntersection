import pickle
import time

import aspectlib

from CommunicationService.Communication import Communication
from Constants import SNOOZE_FACTOR


class ComSend(Communication):

    @aspectlib.Aspect
    def encryptDataAES(self, toBeSent, aesCipher, flag):

        if flag == 'NoAES':
            yield aspectlib.Proceed
        else:
            data = yield aspectlib.Proceed
            yield aspectlib.Return(aesCipher.encrypt(data))

    @aspectlib.Aspect
    def snoozeAdaptivelyTime(self, data):
        yield time.sleep(SNOOZE_FACTOR * len(data))

    def snoozeTime(self, data):
        time.sleep(0.02)

    def processData(self, toBeSent, aesCipher, flag):
        binaryDict = pickle.dumps(toBeSent)
        return binaryDict

    def send(self, toBeSent, ipDestination, portDestination, HEADERSIZE, aesCipher=None, flag=None):

        with aspectlib.weave(self.processData, self.encryptDataAES):
            binaryDict = self.processData(toBeSent, aesCipher, flag)

        socket = self._socketPool.acquire()
        socket.connect((ipDestination, portDestination))

        binaryDict = bytes(f"{len(binaryDict):<{HEADERSIZE}}", 'utf-8') + binaryDict
        socket.send(binaryDict)
        self._socketPool.release(socket)

        with aspectlib.weave(self.snoozeTime, self.snoozeAdaptivelyTime):
            self.snoozeTime(binaryDict)
