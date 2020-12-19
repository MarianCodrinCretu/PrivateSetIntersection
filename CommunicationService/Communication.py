from CommunicationService.SocketPool import SocketPool


class Communication:

    def __init__(self, socketPool: SocketPool):
        self._socketPool = socketPool

    def communicate(self):
        pass
