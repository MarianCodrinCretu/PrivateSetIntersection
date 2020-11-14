from CommunicationService.SocketPool import SocketPool


class Communication:

    def __init__(self, socketPool: SocketPool, aesKey, aesIV):

        self._socketPool = socketPool
        self.aesKey=aesKey.encode("utf8")
        self.aesIV=aesIV.encode("utf8")

    def communicate(self):
        pass