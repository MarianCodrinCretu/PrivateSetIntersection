import os
import pickle
import socket
import threading
import time
from unittest import TestCase

from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from parameterized import parameterized

import Constants
from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol
from CryptoUtils import CryptoUtils


def run_fake_server(address, port, key, iv):
    # Run a server to listen for a connection and then close it
    # inspiration source https://www.devdungeon.com/content/unit-testing-tcp-server-client-python
    time.sleep(0.001)
    server_sock = socket.socket()
    server_sock.bind((address, port))
    server_sock.listen(1)
    server_sock.accept()
    server_sock.close()


bufferZone = ""


def run_fake_client(address, port, message, key, iv, HEADERSIZE, flag, index):
    global bufferZone
    try:
        time.sleep(0.001)
        server_sock = socket.socket()
        server_sock.connect((address, port))
        if flag != 'NoAES':
            cipher = AES.new(key, AES.MODE_CFB, iv)
            message = pickle.dumps(message)
            message = cipher.encrypt(message)
        else:
            if index in (7, 8):
                message = pickle.dumps(CryptoUtils.convertRSAKeyToString(message))
            elif index == 9:
                print(pubKeyServer)
                print(message)
                message = CryptoUtils.rsaEncrypt(pubKeyServer, message)
                message = pickle.dumps(message)
            elif index == 10:
                print(pubKeyClient)
                print(message)
                message = CryptoUtils.rsaEncrypt(pubKeyClient, message)
                message = pickle.dumps(message)
            else:
                message = pickle.dumps(message)
        message = bytes(f"{len(message):<{HEADERSIZE}}", 'utf-8') + message
        server_sock.send(message)
        server_sock.close()
    except ConnectionRefusedError:
        bufferZone = "CONNECTION ERROR"


pubKeyClient = RSA.importKey(open(os.path.join("client_rsa_public.pem")).read())
privKeyClient = RSA.importKey(open(os.path.join("client_rsa_private.pem")).read())
pubKeyServer = RSA.importKey(open(os.path.join("server_rsa_public.pem")).read())
privKeyServer = RSA.importKey(open(os.path.join("server_rsa_private.pem")).read())


class TransferProtocolShould(TestCase):
    _connectionParams = {'Server IP': Constants.SENDER_ADDRESS,
                         'Server Port': Constants.SENDER_PORT,
                         'Client IP': Constants.RECEIVER_ADDRESS,
                         'Client Port': Constants.RECEIVER_PORT}
    comSend = ComSend(SocketPool(20))
    comReceive = ComReceive(SocketPool(20))

    transferProtocol = TransferProtocol(_connectionParams, comSend, comReceive, "Thats my Kung Fu", "ABCDE FG HIJK LM")

    def parametersMapper(self, index):
        if index == 1:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   [], 10, 'NoAES'
        if index == 2:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), \
                   [], 10, 'NoAES'
        if index == 3:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   [{'message': 'I love Quantum Computing', 'message2': 'I love Superposition and Entanglement',
                     'planck': 6.61e-2}], 10, None
        if index == 4:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   [[[i for i in range(10)] for j in range(10)]], 10, None
        if index == 5:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   ["keykeykeykeykey"], 10, None
        if index == 6:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), \
                   [[[i for i in range(10)] for j in range(10)]], 100, None
        if index == 7:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), [pubKeyClient], \
                   50, 'NoAES'
        if index == 8:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), [pubKeyServer], \
                   50, 'NoAES'
        if index == 10:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), [pubKeyServer, self.transferProtocol.aesIV], 10, 'NoAES'
        if index == 9:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), [pubKeyClient, self.transferProtocol.aesKey], 10, 'NoAES'
        if index == 11:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), \
                   [{'message': 'I love Quantum Computing', 'message2': 'I love Superposition and Entanglement',
                     'planck': 6.61e-2}], 10, None
        if index == 12:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), \
                   [str(Exception('Dummy exception'))], 10, None
        if index == 13:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   [str(Exception('Dummy exception'))], 10, None

    def senderMethodMapper(self, index):
        if index == 1:
            return self.transferProtocol.initiateConnection
        if index == 2:
            return self.transferProtocol.sendConfirmationInitiateConnection
        if index == 3:
            return self.transferProtocol.sendNegotiateParameters
        if index == 4:
            return self.transferProtocol.sendOT
        if index == 5:
            return self.transferProtocol.sendPRFKey
        if index == 6:
            return self.transferProtocol.sendPsiValues
        if index == 7:
            return self.transferProtocol.sendRSAReceiverPublicKey
        if index == 8:
            return self.transferProtocol.sendRSASenderPublicKey
        if index == 9:
            return self.transferProtocol.sendAESKeyByRSA
        if index == 10:
            return self.transferProtocol.sendIVByRSA
        if index == 11:
            return self.transferProtocol.sendBackNegotiateParameters
        if index == 12:
            return self.transferProtocol.sendErrorMessageFromSender
        if index == 13:
            return self.transferProtocol.sendErrorMessageFromReceiver

    def receiverMethodMapper(self, index):
        if index == 1:
            return self.transferProtocol.receiveInitiateConnection
        if index == 2:
            return self.transferProtocol.receiveConfirmationInitiateConnection
        if index == 3:
            return self.transferProtocol.receiveNegotiateParameters
        if index == 4:
            return self.transferProtocol.receiveOT
        if index == 5:
            return self.transferProtocol.receiveKey
        if index == 6:
            return self.transferProtocol.receivePsiValues
        if index == 7:
            return self.transferProtocol.receiveRSAReceiverPublicKey
        if index == 8:
            return self.transferProtocol.receiveRSASenderPublicKey
        if index == 9:
            return self.transferProtocol.receiveAESKeyByRSA
        if index == 10:
            return self.transferProtocol.receiveIVByRSA
        if index == 11:
            return self.transferProtocol.receiveModifiedNegotiateParameters
        if index == 12:
            return self.transferProtocol.receiveErrorMessageFromSender
        if index == 13:
            return self.transferProtocol.receiveErrorMessageFromReceiver

    @parameterized.expand([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]])
    def test_sendDesiredDataForEachTestCase(self, index):

        senderFunction = self.senderMethodMapper(index)
        ip, port, parametersList, HEADERSIZE, flag = self.parametersMapper(index)
        server_thread = threading.Thread(target=run_fake_server,
                                         args=(ip, port, self.transferProtocol.aesKey, self.transferProtocol.aesIV))
        server_thread.start()
        time.sleep(0.02)
        if len(parametersList) == 0:
            senderFunction()
        elif len(parametersList) == 2:
            senderFunction(parametersList[1], parametersList[0])
        else:
            senderFunction(parametersList[0])
        server_thread.join()

    @parameterized.expand([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]])
    def test_receiveDesiredDataForEachTestCase(self, index):

        global bufferZone

        receiverFunction = self.receiverMethodMapper(index)
        print(self.parametersMapper(index))
        ip, port, parametersList, HEADERSIZE, flag = self.parametersMapper(index)
        parameter = ""
        receiveParameter = None
        if index == 1:
            parameter = str(self._connectionParams['Client IP'])+' '+str(self._connectionParams['Client Port'])
        elif index == 2:
            parameter = "Received connection attempting! All ok!"
        elif index == 9:
            parameter = self.transferProtocol.aesIV
        elif index == 10:
            parameter = self.transferProtocol.aesKey
        else:
            parameter = parametersList[0]

        if index == 9:
            receiveParameter = privKeyServer
        elif index == 10:
            receiveParameter = privKeyClient
        else:
            receiveParameter = parameter

        client_thread = threading.Thread(target=run_fake_client, args=(
            ip, port, parameter, self.transferProtocol.aesKey, self.transferProtocol.aesIV, HEADERSIZE, flag, index))
        client_thread.start()

        if index not in (9, 10):
            data = receiverFunction()
        else:
            data = receiverFunction(receiveParameter)


        if index==1:
            split = parameter.split(' ')
            toReceive = tuple((split[0], int(split[1])))
            self.assertEqual(data, toReceive)

        elif index not in (9, 10):
            self.assertEqual(data, parameter)

        else:
            self.assertEqual(data, parameter.decode())
        client_thread.join()

        if bufferZone == "CONNECTION ERROR":
            self.fail()

        time.sleep(0.01)
