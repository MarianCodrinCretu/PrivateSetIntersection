from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool
import pickle


# TransferProtocol Communication Class
# @author mcretu
class TransferProtocol:

    # connectionParams is a dictionary with parameters connection
    #
    def __init__(self, connectionParams, comSend: ComSend, comReceive: ComReceive):
        self._connectionParams = connectionParams
        self._comSend = comSend
        self._comReceive = comReceive

    # function for sending parameters in negotiation process
    # @param paramsDictionary the dictionary of negotiation parameters
    # {'lambda': int, 'sigma':int, 'm':int, 'w':int, 'l1':int, 'l2':int, 'hash1':string, 'hash2':string, 'PRF':string}

    def initiateConnection(self):
        self._comSend.send("Connection attempting!", self._connectionParams['Server IP'],
                           int(self._connectionParams['Server Port']),
                           HEADERSIZE=10)

    def receiveInitiateConnection(self):
        return self._comReceive.receive(self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                                        HEADERSIZE=10)

    def sendConfirmationInitiateConnection(self):
        self._comSend.send("Received connection attempting! All ok!", self._connectionParams['Client IP'],
                           int(self._connectionParams['Client Port']),
                           HEADERSIZE=10)

    def receiveConfirmationInitiateConnection(self):
        return self._comReceive.receive(self._connectionParams['Client IP'],
                                        int(self._connectionParams['Client Port']),
                                        HEADERSIZE=10)

    def sendNegotiateParameters(self, paramsDictionary):
        self._comSend.send(paramsDictionary, self._connectionParams['Server IP'],
                           int(self._connectionParams['Server Port']),
                           HEADERSIZE=10)

    def receiveNegotiateParameters(self):
        return self._comReceive.receive(self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                                        HEADERSIZE=10)

    def sendOT(self, data):
        self._comSend.send(data, self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                           HEADERSIZE=10)

    def receiveOT(self):
        return self._comReceive.receive(self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                                        HEADERSIZE=10)

    def sendPRFKey(self, key):
        self._comSend.send(key, self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                           HEADERSIZE=10)

    def receiveKey(self):
        return self._comReceive.receive(self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                                        HEADERSIZE=10)

    def sendPsiValues(self, data):
        self._comSend.send(data, self._connectionParams['Client IP'], int(self._connectionParams['Client Port']),
                           HEADERSIZE=100)

    def receivePsiValues(self):
        return self._comReceive.receive(self._connectionParams['Client IP'], int(self._connectionParams['Client Port']),
                                        HEADERSIZE=100)

    # def send(self, toBeSent, ipDestination, portDestination, HEADERSIZE):
    #
    #     binaryDict = pickle.dumps(toBeSent)
    #
    #     socket = self._socketPool.acquire()
    #     socket.connect((ipDestination, portDestination))
    #
    #     binaryDict= bytes(f"{len(binaryDict):<{HEADERSIZE}}", 'utf-8')+binaryDict
    #     socket.send(binaryDict)
    #     #self._socketPool.release(socket)
    #
    # def receive(self, ipToReceive, portToReceive, HEADERSIZE, sizeOfDgram=16):
    #
    #     socket = self._socketPool.acquire()
    #     socket.bind((ipToReceive, int(portToReceive)))
    #     socket.listen(5)
    #
    #     connection, address = socket.accept()
    #
    #     receivedObject = b''
    #     newMessage = True
    #     msglen = 0
    #     while(True):
    #         msg = connection.recv(sizeOfDgram)
    #         if newMessage:
    #             msglen = int(msg[:HEADERSIZE])
    #             newMessage = False
    #
    #         receivedObject += msg
    #
    #         if len(receivedObject) - HEADERSIZE == msglen:
    #             #self._socketPool.release(socket)
    #             return pickle.loads(receivedObject[HEADERSIZE:])
    #
    # #######################################################################################################
