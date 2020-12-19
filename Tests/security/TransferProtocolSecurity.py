import os
import pickle
import socket
import threading
import time
from unittest import TestCase

from Crypto.PublicKey import RSA
from parameterized import parameterized
from Crypto.Cipher import AES

import Constants
from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol
from CryptoUtils import CryptoUtils

bufferZone = ""

import binascii
import numpy
import math

def convertToBytes(ini_string):

    # Code to convert hex to binary
    return bin(int.from_bytes(ini_string, byteorder="big")).strip('0b')

def DFTStatisticalTest(sequence, confidence=0.99, decisionLevel=0.001):

    sequence = [int(x) for x in sequence]
    n=len(sequence)

    dftSequence = numpy.fft.fft(sequence)

    sprim = dftSequence[:int(numpy.floor(len(dftSequence)/2 + 0.5))]

    m = numpy.abs(sprim)

    T = numpy.sqrt(n*numpy.log10(1/(1-confidence)))
    N0 = confidence*n/2
    N1 = len(m[m < T])

    d = (N1-N0)/numpy.sqrt(n*confidence*(1-confidence)/4)

    pValue= math.erfc(numpy.abs(d)/numpy.sqrt(2))

    # return True if we have no clue that the sequence is not random
    # if pValue is less than decisionLevel, then we will return False
    print(pValue)
    return pValue >= decisionLevel

def run_fake_client(address, port, message, key, iv, HEADERSIZE, flag, index):
    global bufferZone
    try:
        time.sleep(0.001)
        server_sock = socket.socket()
        server_sock.connect((address, port))
        if flag!='NoAES':
            cipher = AES.new(key, AES.MODE_CFB, iv)
            message = pickle.dumps(message)
            message = cipher.encrypt(message)
        message = bytes(f"{len(message):<{HEADERSIZE}}", 'utf-8') + message
        server_sock.send(message)
        server_sock.close()
    except ConnectionRefusedError:
        bufferZone = "CONNECTION ERROR"

pubKeyClient = RSA.importKey(open(os.path.join("client_rsa_public.pem")).read())
privKeyClient = RSA.importKey(open(os.path.join("client_rsa_private.pem")).read())
pubKeyServer = RSA.importKey(open(os.path.join("client_rsa_public.pem")).read())
privKeyServer = RSA.importKey(open(os.path.join("client_rsa_private.pem")).read())

class TransferProtocolSecurity(TestCase):
    _connectionParams = {'Server IP': Constants.SENDER_ADDRESS,
                         'Server Port': Constants.SENDER_PORT,
                         'Client IP': Constants.RECEIVER_ADDRESS,
                         'Client Port': Constants.RECEIVER_PORT}

    aesKey = "Thats my Kung Fu"
    aesIV = "ABCDE FG HIJK LM"
    comSend = ComSend(SocketPool(20))
    comReceive = ComReceive(SocketPool(20))

    transferProtocol = TransferProtocol(_connectionParams, comSend, comReceive, aesKey, aesIV)

    def test_statisticalNIST(self):
        with open('security.txt', 'r') as filex:
            totalData = filex.read()
            data = totalData.split('\n--------------------\n')[:-1]

            for dataElement in data:
                databytes = convertToBytes(dataElement[1:].encode())
                print(DFTStatisticalTest(databytes))
                self.assertTrue(DFTStatisticalTest(databytes))

    def parametersMapper(self, index):
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
        if index == 11:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), \
                   [{'message': 'I love Quantum Computing', 'message2': 'I love Superposition and Entanglement',
                     'planck': 6.61e-2}], 10, None

    def receiverMethodMapper(self, index):
        if index == 3:
            return self.transferProtocol.receiveNegotiateParameters
        if index == 4:
            return self.transferProtocol.receiveOT
        if index == 5:
            return self.transferProtocol.receiveKey
        if index == 6:
            return self.transferProtocol.receivePsiValues
        if index == 11:
            return self.transferProtocol.receiveModifiedNegotiateParameters


    @parameterized.expand([ [3], [4], [5], [6], [11]])
    def test_receiveDesiredDataForEachTestCase(self, index):

        global bufferZone

        receiverFunction = self.receiverMethodMapper(index)
        print(self.parametersMapper(index))
        ip, port, parametersList, HEADERSIZE, flag = self.parametersMapper(index)

        parameter = parametersList[0]

        client_thread = threading.Thread(target=run_fake_client, args=(
        ip, port, parameter, self.transferProtocol.aesKey, self.transferProtocol.aesIV, HEADERSIZE, flag, index))
        client_thread.start()

        data = receiverFunction()

        self.assertEqual(data, parameter)

        client_thread.join()

        if bufferZone == "CONNECTION ERROR":
            self.fail()

        time.sleep(0.01)

