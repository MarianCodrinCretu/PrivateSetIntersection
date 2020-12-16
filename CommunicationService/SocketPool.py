import socket

class SocketPool:

    def __init__ (self, size):

        if isinstance(size, int) or isinstance(size, float):
            if int(size)<10:
                size=10
            else:
                size=int(size)
        else:
            size=10
        self._socketPools=[socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in range(size)]
        for index in range(size):
            self._socketPools[index].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def acquire(self):

        return self._socketPools.pop()

    def release(self, reusableSocket):
        reusableSocket.close()
        if len(self._socketPools)==0:
            socketToAppend=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socketToAppend.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self._socketPools.append(socketToAppend)


