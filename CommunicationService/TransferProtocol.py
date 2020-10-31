from CommunicationService.SocketPool import SocketPool
import pickle

# TransferProtocol Communication Class
# @author mcretu
class TransferProtocol:

    #connectionParams is a dictionary with parameters connection
    #
    def __init__(self, socketPool: SocketPool, connectionParams):
        self._socketPool = socketPool
        self._connectionParams = connectionParams

    # function for sending parameters in negotiation process
    # @param paramsDictionary the dictionary of negotiation parameters
    # {'lambda': int, 'sigma':int, 'm':int, 'w':int, 'l1':int, 'l2':int, 'hash1':string, 'hash2':string, 'PRF':string}

    def sendNegotiateParameters(self, paramsDictionary):

        self.send(paramsDictionary, self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                  HEADERSIZE=10 )

    def receiveNegotiateParameters(self):

        return self.receive(self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                            HEADERSIZE=10)

    def sendOT(self, data):

        self.send(data, self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                  HEADERSIZE=100 )

    def receiveOT(self):

        return self.receive(self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                            HEADERSIZE=100)

    def sendPRFKey(self, key):

        self.send(key, self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                  HEADERSIZE=10 )

    def receiveKey(self):

        return self.receive(self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                            HEADERSIZE=10)

    def sendPsiValues(self, data):

        self.send(data, self._connectionParams['Client IP'], int(self._connectionParams['Client Port']),
                  HEADERSIZE=100 )

    def receivePsiValues(self):

        return self.receive(self._connectionParams['Client IP'], int(self._connectionParams['Client Port']),
                            HEADERSIZE=100)


    def send(self, toBeSent, ipDestination, portDestination, HEADERSIZE):

        binaryDict = pickle.dumps(toBeSent)

        socket = self._socketPool.acquire()
        socket.connect((ipDestination, portDestination))

        binaryDict= bytes(f"{len(binaryDict):<{HEADERSIZE}}", 'utf-8')+binaryDict
        socket.send(binaryDict)
        #self._socketPool.release(socket)

    def receive(self, ipToReceive, portToReceive, HEADERSIZE, sizeOfDgram=16):

        socket = self._socketPool.acquire()
        socket.bind((ipToReceive, int(portToReceive)))
        socket.listen(5)

        connection, address = socket.accept()

        receivedObject = b''
        newMessage = True
        msglen = 0
        while(True):
            msg = connection.recv(sizeOfDgram)
            if newMessage:
                msglen = int(msg[:HEADERSIZE])
                newMessage = False

            receivedObject += msg

            if len(receivedObject) - HEADERSIZE == msglen:
                #self._socketPool.release(socket)
                return pickle.loads(receivedObject[HEADERSIZE:])

    #######################################################################################################



