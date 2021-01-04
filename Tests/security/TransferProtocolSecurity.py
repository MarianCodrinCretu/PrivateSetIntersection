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
import CryptoUtils

def convertToBytes(ini_string):

    # Code to convert hex to binary
    return bin(int.from_bytes(ini_string, byteorder="big")).strip('0b')

def DFTStatisticalTest(sequence, confidence=0.95, decisionLevel = 0.01 ):

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
    return pValue >= decisionLevel


pubKeyClient = RSA.importKey(open(os.path.join("client_rsa_public.pem")).read())
privKeyClient = RSA.importKey(open(os.path.join("client_rsa_private.pem")).read())
pubKeyServer = RSA.importKey(open(os.path.join("server_rsa_private.pem")).read())
privKeyServer = RSA.importKey(open(os.path.join("server_rsa_private.pem")).read())

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

        for fileName in ['aesAnalysis.txt']:
            with open(fileName, 'r') as filex:
                totalData = filex.read()
                data = totalData.split('\n--------------------\n')[:-1]

                for dataElement in data:
                    databytes = convertToBytes(dataElement[1:].encode())
                    self.assertTrue(DFTStatisticalTest(databytes,confidence=0.991, decisionLevel=0.0001))

    def test_rsaStatisticalNIST(self):

        for fileName in ['rsaAnalysisReceive.txt', 'rsaAnalysisSend.txt']:
            with open(fileName, 'r') as filex:
                totalData = filex.read()
                data = totalData.split('\n--------------------\n')[:-1]

                for dataElement in data:
                    databytes = convertToBytes(dataElement[1:].encode())
                    self.assertTrue(DFTStatisticalTest(databytes,confidence=0.99, decisionLevel=1.0e-8))

    def test_aesCheck(self):
        for fileName in ['aesAnalysis.txt']:
            with open(fileName, 'r') as filex:
                totalData = filex.read()
                data = totalData.split('\n--------------------\n')[:-1]

                for dataElement in data:
                    cipher = AES.new(self.aesKey.encode('utf8'), AES.MODE_CFB, self.aesIV.encode('utf8'))

                    cipher.decrypt(dataElement.encode('utf8'))


    def test_rsaCheck(self):

        for fileName in ['rsaAnalysisIv', 'rsaAnalysisKey']:
            with open(fileName, 'rb') as filex:
                totalData = filex.read()
                if fileName=='rsaAnalysisIv':
                    datax = CryptoUtils.CryptoUtils.rsaDecrypt(privKeyServer, totalData)
                    self.assertEqual(self.aesIV.encode('utf8'), datax.encode('utf8'))
                else:
                    datax = CryptoUtils.CryptoUtils.rsaDecrypt(privKeyClient, totalData)
                    self.assertEqual(self.aesKey.encode('utf8'), datax.encode('utf8'))









