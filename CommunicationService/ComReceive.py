import pickle

from CommunicationService.Communication import Communication


class ComReceive(Communication):

    def receive(self, ipToReceive, portToReceive, HEADERSIZE, sizeOfDgram=16):

        socket = self._socketPool.acquire()
        socket.bind((ipToReceive, int(portToReceive)))
        socket.listen(5)

        connection, address = socket.accept()

        receivedObject = b''
        newMessage = True
        msglen = 0
        while (True):
            msg = connection.recv(sizeOfDgram)
            if newMessage:
                msglen = int(msg[:HEADERSIZE])
                newMessage = False

            receivedObject += msg

            if len(receivedObject) - HEADERSIZE == msglen:
                self._socketPool.release(socket)
                return pickle.loads(receivedObject[HEADERSIZE:])

