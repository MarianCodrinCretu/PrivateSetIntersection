import pickle
import socket
import threading
import time
from unittest import TestCase
from parameterized import parameterized
from Crypto.Cipher import AES

import Constants
from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol


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


def run_fake_client(address, port, message, key, iv, HEADERSIZE):
    global bufferZone
    try:
        time.sleep(0.001)
        server_sock = socket.socket()
        server_sock.connect((address, port))
        cipher = AES.new(key, AES.MODE_CFB, iv)
        message = pickle.dumps(message)
        message = cipher.encrypt(message)
        message = bytes(f"{len(message):<{HEADERSIZE}}", 'utf-8') + message
        server_sock.send(message)
        server_sock.close()
    except ConnectionRefusedError:
        bufferZone = "CONNECTION ERROR"


class TransferProtocolShould(TestCase):
    _connectionParams = {'Server IP': Constants.SENDER_ADDRESS,
                         'Server Port': Constants.SENDER_PORT,
                         'Client IP': Constants.RECEIVER_ADDRESS,
                         'Client Port': Constants.RECEIVER_PORT}
    comSend = ComSend(SocketPool(20), "Thats my Kung Fu", "ABCDE FG HIJK LM")
    comReceive = ComReceive(SocketPool(20),"Thats my Kung Fu", "ABCDE FG HIJK LM")

    transferProtocol = TransferProtocol(_connectionParams, comSend, comReceive)

    def parametersMapper(self, index):
        if index == 1:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   [], 10
        if index == 2:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), \
                   [], 10
        if index == 3:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   [{'message': 'I love Quantum Computing', 'message2': 'I love Superposition and Entanglement',
                     'planck': 6.61e-2}], 10
        if index == 4:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   [[[i for i in range(10)] for j in range(10)]], 10
        if index == 5:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   ["keykeykeykeykey"], 10
        if index == 6:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), \
                   [[[i for i in range(10)] for j in range(10)]], 100

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

    @parameterized.expand([[1], [2], [3], [4], [5], [6]])
    def test_sendDesiredDataForEachTestCase(self, index):

        senderFunction = self.senderMethodMapper(index)
        ip, port, parametersList, HEADERSIZE = self.parametersMapper(index)
        server_thread = threading.Thread(target=run_fake_server, args=(ip, port, self.comSend.aesKey, self.comSend.aesIV))
        server_thread.start()
        time.sleep(0.02)
        if len(parametersList) == 0:
            senderFunction()
        else:
            senderFunction(parametersList[0])
        server_thread.join()

    @parameterized.expand([[1], [2], [3], [4], [5], [6]])
    def test_receiveDesiredDataForEachTestCase(self, index):

        global bufferZone

        receiverFunction = self.receiverMethodMapper(index)
        ip, port, parametersList, HEADERSIZE = self.parametersMapper(index)

        parameter = ""
        if index == 1:
            parameter = "Connection attempting!"
        elif index == 2:
            parameter = "Received connection attempting! All ok!"
        else:
            parameter = parametersList[0]

        client_thread = threading.Thread(target=run_fake_client, args=(ip, port, parameter, self.comReceive.aesKey,self.comReceive.aesIV, HEADERSIZE))
        client_thread.start()

        data = receiverFunction()
        self.assertEqual(data, parameter)
        client_thread.join()

        if bufferZone == "CONNECTION ERROR":
            self.fail()

        time.sleep(0.01)
