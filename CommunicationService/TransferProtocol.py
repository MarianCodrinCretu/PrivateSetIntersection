from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
import CryptoUtils.CryptoUtils

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
                           HEADERSIZE=10, flag='NoAES')

    def sendConfirmationInitiateConnection(self):
        self._comSend.send("Received connection attempting! All ok!", self._connectionParams['Client IP'],
                           int(self._connectionParams['Client Port']),
                           HEADERSIZE=10, flag='NoAES')

    def sendRSAReceiverPublicKey(self, key):
        key = CryptoUtils.CryptoUtils.convertRSAKeyToString(key)
        self._comSend.send(key, self._connectionParams['Server IP'],
                           int(self._connectionParams['Server Port']),
                           HEADERSIZE=50, flag='NoAES')

    def receiveRSAReceiverPublicKey(self):

        result= self._comReceive.receive(self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                                        HEADERSIZE=50, flag='NoAES')
        return CryptoUtils.CryptoUtils.stringToRSAKey(result)

    def sendRSASenderPublicKey(self, key):
        key = CryptoUtils.CryptoUtils.convertRSAKeyToString(key)
        self._comSend.send(key, self._connectionParams['Client IP'],
                           int(self._connectionParams['Client Port']),
                           HEADERSIZE=50, flag='NoAES')


    def receiveRSASenderPublicKey(self):
        result = self._comReceive.receive(self._connectionParams['Client IP'], int(self._connectionParams['Client Port']),
                                        HEADERSIZE=50, flag='NoAES')
        return CryptoUtils.CryptoUtils.stringToRSAKey(result)



    def sendIVByRSA(self, iv, rsaKey):
        iv = CryptoUtils.CryptoUtils.rsaEncrypt(rsaKey, iv)
        self._comSend.send(iv, self._connectionParams['Server IP'],
                           int(self._connectionParams['Server Port']),
                           HEADERSIZE=10, flag='NoAES')

    def receiveIVByRSA(self, rsaKey):
        return CryptoUtils.CryptoUtils.rsaDecrypt(
            rsaKey, self._comReceive.receive(self._connectionParams['Server IP'],  int(self._connectionParams['Server Port']),
                                        HEADERSIZE=10, flag='NoAES'))

    def sendAESKeyByRSA(self, aesKey, rsaKey):
        aesKey = CryptoUtils.CryptoUtils.rsaEncrypt(rsaKey, aesKey)
        self._comSend.send(aesKey, self._connectionParams['Client IP'],
                           int(self._connectionParams['Client Port']),
                           HEADERSIZE=10, flag='NoAES')

    def receiveAESKeyByRSA(self, rsaKey):
        return CryptoUtils.CryptoUtils.rsaDecrypt(rsaKey,
                                                  self._comReceive.receive
                                                  (self._connectionParams['Client IP'], int(self._connectionParams['Client Port']),
                                        HEADERSIZE=10, flag='NoAES'))







    def sendNegotiateParameters(self, paramsDictionary):
        self._comSend.send(paramsDictionary, self._connectionParams['Server IP'],
                           int(self._connectionParams['Server Port']),
                           HEADERSIZE=10)

    def sendOT(self, data):
        self._comSend.send(data, self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                           HEADERSIZE=10)

    def sendPRFKey(self, key):
        self._comSend.send(key, self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                           HEADERSIZE=10)

    def sendPsiValues(self, data):
        self._comSend.send(data, self._connectionParams['Client IP'], int(self._connectionParams['Client Port']),
                           HEADERSIZE=100)


    def receiveInitiateConnection(self):
        return self._comReceive.receive(self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                                        HEADERSIZE=10, flag='NoAES')


    def receiveConfirmationInitiateConnection(self):
        return self._comReceive.receive(self._connectionParams['Client IP'],
                                        int(self._connectionParams['Client Port']),
                                        HEADERSIZE=10, flag='NoAES')

    def receiveNegotiateParameters(self):
        return self._comReceive.receive(self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                                        HEADERSIZE=10)

    def receiveOT(self):
        return self._comReceive.receive(self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                                        HEADERSIZE=10)

    def receiveKey(self):
        return self._comReceive.receive(self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                                        HEADERSIZE=10)

    def receivePsiValues(self):
        return self._comReceive.receive(self._connectionParams['Client IP'], int(self._connectionParams['Client Port']),
                                        HEADERSIZE=100)

