import socket
import time

class SocketPool:

    def __init__ (self, size):

        self._socketPools=[socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in range(size)]

    def acquire(self):
        # for socketElement in self._socketPools:
        #     if socketElement.type != None:

        return self._socketPools.pop()

    def release(self, reusableSocket):
        reusableSocket.close()
        self._socketPools.append(reusableSocket)


