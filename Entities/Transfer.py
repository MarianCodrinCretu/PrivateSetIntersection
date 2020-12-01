import time
import pickle
import socket


class Transfer_Protocol:
    def __init__(self, connectionParams):
        self._connectionParams = {
            "Server IP": '127.0.0.1',
            "Server Port": 5585,
            "Client IP": '127.0.0.1',
            "Client Port": 5586
        }
        self._socketPool = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in range(5)]

    def processDataS(self, toBeSent, flag):
        binaryDict = pickle.dumps(toBeSent)
        return binaryDict

    def processDataR(self, data, flag):
        data = pickle.loads(data)
        return data

    def send(self, toBeSent, ipDestination, portDestination, HEADERSIZE, flag=None):
        binaryDict = self.processDataS(toBeSent, flag)

        socket = self._socketPool.pop()
        socket.connect((ipDestination, portDestination))

        binaryDict = bytes(f"{len(binaryDict):<{HEADERSIZE}}", 'utf-8') + binaryDict
        socket.send(binaryDict)
        socket.close()

        time.sleep(0.2)

    def receive(self, ipToReceive, portToReceive, HEADERSIZE, sizeOfDgram=16, flag=None):

        socket = self._socketPool.pop()
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
                socket.close()
                data = receivedObject[HEADERSIZE:]

                return self.processDataR(data, flag)

    def send_OT(self, data):
        self.send(data, self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                           HEADERSIZE=10)

    def receiveOT(self):
        result = self.receive(self._connectionParams['Server IP'],
                                          int(self._connectionParams['Server Port']),
                                          HEADERSIZE=10)
        return result
