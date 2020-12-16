from CommunicationService.SocketPool import SocketPool
import string
import random

class Communication:

    def __init__(self, socketPool: SocketPool, aesKey, aesIV):

        self._socketPool = socketPool
        if aesKey is None or len(aesKey)!=16:
            self.aesKey = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 16))
        if aesIV is None or len(aesIV)!=16:
            self.aesIV = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 16))
        self.aesKey=aesKey.encode("utf8")
        self.aesIV=aesIV.encode("utf8")

    def communicate(self):
        pass