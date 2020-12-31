import csv

import aspectlib
from Crypto.Cipher import AES
from aspectlib import Aspect

import CryptoUtils.CryptoUtils
import Logs.LogMessaging
from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend


# TransferProtocol Communication Class
# @author mcretu


class TransferProtocol:

    # connectionParams is a dictionary with parameters connection
    #
    def __init__(self, connectionParams, comSend: ComSend, comReceive: ComReceive, aesKey=None, aesIV=None):
        self._connectionParams = connectionParams
        self._comSend = comSend
        self._comReceive = comReceive
        if aesKey is None or len(aesKey) != 16:
            aesKey = CryptoUtils.CryptoUtils.generateAESKey()
        if aesIV is None or len(aesIV) != 16:
            aesIV = CryptoUtils.CryptoUtils.generateAESIv()
        self.aesKey = aesKey.encode("utf8")
        self.aesIV = aesIV.encode("utf8")

    @Aspect
    def log_results(self, message):
        data = yield aspectlib.Proceed
        if message[1] == 'SENDER':
            file = 'communicationLogsSender.csv'
        else:
            file = 'communicationLogsReceiver.csv'
        with open(file, mode='a') as log:
            log_writer = csv.writer(log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            log_writer.writerow([message[0], message[1], message[2], message[3]])

    def processMessage(self, message):
        print("%s--%s--%s--%s" % (message[0], message[1], message[2], message[3]))

    # function for sending parameters in negotiation process
    # @param paramsDictionary the dictionary of negotiation parameters
    # {'lambda': int, 'sigma':int, 'm':int, 'w':int, 'l1':int, 'l2':int, 'hash1':string, 'hash2':string, 'PRF':string}

    def initiateConnection(self):
        self._comSend.send(str(self._connectionParams['Client IP'])+' '+str(self._connectionParams['Client Port']),
                           self._connectionParams['Server IP'],
                           int(self._connectionParams['Server Port']),
                           HEADERSIZE=10, flag='NoAES')
        message = Logs.LogMessaging.createLogInitiateMessage(self._connectionParams['Server IP'],
                                                             self._connectionParams['Server Port'])

        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

    def sendConfirmationInitiateConnection(self):
        self._comSend.send("Received connection attempting! All ok!", self._connectionParams['Client IP'],
                           int(self._connectionParams['Client Port']),
                           HEADERSIZE=10, flag='NoAES')
        message = Logs.LogMessaging.createLogSendConfirmationMessage(self._connectionParams['Client IP'],
                                                                     self._connectionParams['Client Port'],
                                                                     self._connectionParams['Server IP'],
                                                                     self._connectionParams['Server Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

    def sendRSAReceiverPublicKey(self, key):

        key = CryptoUtils.CryptoUtils.convertRSAKeyToString(key)
        self._comSend.send(key, self._connectionParams['Server IP'],
                           int(self._connectionParams['Server Port']),
                           HEADERSIZE=50, flag='NoAES')
        message = Logs.LogMessaging.createLogSendReceiverRSA(self._connectionParams['Server IP'],
                                                             self._connectionParams['Server Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

    def receiveRSAReceiverPublicKey(self):

        result = self._comReceive.receive(self._connectionParams['Server IP'],
                                          int(self._connectionParams['Server Port']),
                                          HEADERSIZE=50, flag='NoAES')
        message = Logs.LogMessaging.createLogReceiveReceiverRSA(self._connectionParams['Client IP'],
                                                                self._connectionParams['Client Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)
        return CryptoUtils.CryptoUtils.stringToRSAKey(result)

    def sendRSASenderPublicKey(self, key):

        key = CryptoUtils.CryptoUtils.convertRSAKeyToString(key)
        self._comSend.send(key, self._connectionParams['Client IP'],
                           int(self._connectionParams['Client Port']),
                           HEADERSIZE=50, flag='NoAES')
        message = Logs.LogMessaging.createLogSendSenderRSA(self._connectionParams['Client IP'],
                                                           self._connectionParams['Client Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

    def receiveRSASenderPublicKey(self):

        result = self._comReceive.receive(self._connectionParams['Client IP'],
                                          int(self._connectionParams['Client Port']),
                                          HEADERSIZE=50, flag='NoAES')
        message = Logs.LogMessaging.createLogReceiveReceiverRSA(self._connectionParams['Server IP'],
                                                                self._connectionParams['Server Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)
        return CryptoUtils.CryptoUtils.stringToRSAKey(result)

    def sendIVByRSA(self, iv, rsaKey):

        self.aesIV = iv
        iv = CryptoUtils.CryptoUtils.rsaEncrypt(rsaKey, iv)
        self._comSend.send(iv, self._connectionParams['Server IP'],
                           int(self._connectionParams['Server Port']),
                           HEADERSIZE=10, flag='NoAES')
        message = Logs.LogMessaging.createLogSendIV(self._connectionParams['Server IP'],
                                                    self._connectionParams['Server Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

    def receiveIVByRSA(self, rsaKey):

        result = self._comReceive.receive(self._connectionParams['Server IP'],
                                          int(self._connectionParams['Server Port']),
                                          HEADERSIZE=10, flag='NoAES')
        message = Logs.LogMessaging.createLogReceiveIV(self._connectionParams['Client IP'],
                                                       self._connectionParams['Client Port'])

        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)
        result = CryptoUtils.CryptoUtils.rsaDecrypt(rsaKey, result)
        self.aesIV = result.encode('utf8')
        return result

    def sendAESKeyByRSA(self, aesKey, rsaKey):
        self.aesKey = aesKey
        aesKey = CryptoUtils.CryptoUtils.rsaEncrypt(rsaKey, aesKey)
        self._comSend.send(aesKey, self._connectionParams['Client IP'],
                           int(self._connectionParams['Client Port']),
                           HEADERSIZE=10, flag='NoAES')
        message = Logs.LogMessaging.createLogSendKey(self._connectionParams['Client IP'],
                                                     self._connectionParams['Client Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

    def receiveAESKeyByRSA(self, rsaKey):
        result = self._comReceive.receive(self._connectionParams['Client IP'],
                                          int(self._connectionParams['Client Port']),
                                          HEADERSIZE=10, flag='NoAES')
        message = Logs.LogMessaging.createLogReceiveIV(self._connectionParams['Server IP'],
                                                       self._connectionParams['Server Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)
        result = CryptoUtils.CryptoUtils.rsaDecrypt(rsaKey, result)
        self.aesKey = result.encode('utf8')
        return result

    def sendNegotiateParameters(self, paramsDictionary):
        self._comSend.send(paramsDictionary, self._connectionParams['Server IP'],
                           int(self._connectionParams['Server Port']),
                           HEADERSIZE=10, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.createLogSendNegociate(self._connectionParams['Server IP'],
                                                           self._connectionParams['Server Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

    def sendBackNegotiateParameters(self, paramsDictionary):
        self._comSend.send(paramsDictionary, self._connectionParams['Client IP'],
                           int(self._connectionParams['Client Port']),
                           HEADERSIZE=10, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.createLogSendBackNegociate(self._connectionParams['Client IP'],
                                                               self._connectionParams['Client Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

    def sendOT(self, data):

        self._comSend.send(data, self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                           HEADERSIZE=10, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.createLogSendOT(self._connectionParams['Server IP'],
                                                    self._connectionParams['Server Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

    def sendPRFKey(self, key):

        self._comSend.send(key, self._connectionParams['Server IP'], int(self._connectionParams['Server Port']),
                           HEADERSIZE=10, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.createLogSendPRFKey(self._connectionParams['Server IP'],
                                                        self._connectionParams['Server Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

    def sendPsiValues(self, data):

        self._comSend.send(data, self._connectionParams['Client IP'], int(self._connectionParams['Client Port']),
                           HEADERSIZE=100, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.createLogSendPsiValues(self._connectionParams['Client IP'],
                                                           self._connectionParams['Client Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

    # -------------------------------------------------------------

    def receiveInitiateConnection(self):
        result = self._comReceive.receive(self._connectionParams['Server IP'],
                                          int(self._connectionParams['Server Port']),
                                          HEADERSIZE=10, flag='NoAES')
        message = Logs.LogMessaging.createLogReceiveInitConnection(self._connectionParams['Client IP'],
                                                                   self._connectionParams['Client Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

        ip = result[0]
        port = result[1]
        return ip,port

    def receiveConfirmationInitiateConnection(self):
        result = self._comReceive.receive(self._connectionParams['Client IP'],
                                          int(self._connectionParams['Client Port']),
                                          HEADERSIZE=10, flag='NoAES')
        message = Logs.LogMessaging.createLogReceiveConfirmConnection(self._connectionParams['Server IP'],
                                                                      self._connectionParams['Server Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)
        return result

    def receiveNegotiateParameters(self):
        result = self._comReceive.receive(self._connectionParams['Server IP'],
                                          int(self._connectionParams['Server Port']),
                                          HEADERSIZE=10, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.createLogReceiveNegParameters(self._connectionParams['Client IP'],
                                                                  self._connectionParams['Client Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)
        return result

    def receiveModifiedNegotiateParameters(self):
        result = self._comReceive.receive(self._connectionParams['Client IP'],
                                          int(self._connectionParams['Client Port']),
                                          HEADERSIZE=10, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.createModifiedLogReceiveNegParameters(self._connectionParams['Server IP'],
                                                                          self._connectionParams['Server Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)
        return result

    def receiveOT(self):
        result = self._comReceive.receive(self._connectionParams['Server IP'],
                                          int(self._connectionParams['Server Port']),
                                          HEADERSIZE=10, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.createLogReceiveOT(self._connectionParams['Client IP'],
                                                       self._connectionParams['Client Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)
        return result

    def receiveKey(self):
        result = self._comReceive.receive(self._connectionParams['Server IP'],
                                          int(self._connectionParams['Server Port']),
                                          HEADERSIZE=10, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.createLogReceivePRFKey(self._connectionParams['Client IP'],
                                                           self._connectionParams['Client Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)
        return result

    def receivePsiValues(self):
        result = self._comReceive.receive(self._connectionParams['Client IP'],
                                          int(self._connectionParams['Client Port']),
                                          HEADERSIZE=100, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.createLogReceivePsi(self._connectionParams['Server IP'],
                                                        self._connectionParams['Server Port'])
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)
        return result

    ######################################## ERROR MESSAGING MANAGING ###################################################
    def sendErrorMessageFromSender(self, e, headersize=10):
        self._comSend.send("EXCEPTION FROM SENDER: " +str(e), self._connectionParams['Client IP'],
                           int(self._connectionParams['Client Port']),
                           HEADERSIZE=10, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.exceptionSender(str(e))
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

    def receiveErrorMessageFromSender(self, headersize=10):
        result = self._comReceive.receive(self._connectionParams['Client IP'],
                                          int(self._connectionParams['Client Port']),
                                          HEADERSIZE=headersize, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.receivedExceptionFromSender(str(result))
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)
        return result

    def sendErrorMessageFromReceiver(self, e, headersize=10):
        self._comSend.send("EXCEPTION FROM RECEIVER: "+ str(e), self._connectionParams['Server IP'],
                           int(self._connectionParams['Server Port']),
                           HEADERSIZE=headersize, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.exceptionReceiver(str(e))
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)

    def receiveErrorMessageFromReceiver(self, headersize=10):
        result = self._comReceive.receive(self._connectionParams['Server IP'],
                                          int(self._connectionParams['Server Port']),
                                          HEADERSIZE=headersize, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        message = Logs.LogMessaging.receivedExceptionFromReceiver(str(result))
        with aspectlib.weave(self.processMessage, self.log_results):
            self.processMessage(message)
        return result

    def sendFinalOk(self):
        self._comSend.send("RECEIVER: ALGORITHM FINISHED!", self._connectionParams['Server IP'],
                           int(self._connectionParams['Server Port']),
                           HEADERSIZE=10, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))

    def receiveFinalOk(self):
        result = self._comReceive.receive(self._connectionParams['Server IP'],
                                          int(self._connectionParams['Server Port']),
                                          HEADERSIZE=10, aesCipher=AES.new(self.aesKey, AES.MODE_CFB, self.aesIV))
        return result
