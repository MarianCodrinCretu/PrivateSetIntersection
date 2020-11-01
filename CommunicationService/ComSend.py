import pickle

from CommunicationService.Communication import Communication


class ComSend(Communication):

    def send(self, toBeSent, ipDestination, portDestination, HEADERSIZE):

        binaryDict = pickle.dumps(toBeSent)

        socket = self._socketPool.acquire()
        socket.connect((ipDestination, portDestination))

        binaryDict = bytes(f"{len(binaryDict):<{HEADERSIZE}}", 'utf-8') + binaryDict
        socket.send(binaryDict)
        #self._socketPool.release(socket)
