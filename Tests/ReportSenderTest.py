

import os
from unittest import TestCase

import parameterized
from Crypto.PublicKey import RSA

import Constants
from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol
from DataEngineeringService.CSVParser import CSVParser
from DataEngineeringService.DataEngineering import DataEngineering
from DataEngineeringService.XLSParser import XLSParser
from NegotiationParameters.NegotiateParameters import NegociateParameters
from NegotiationParameters.NegotiateParametersUtils import NegotiateParametersUtils
from NucleusAlgorithm.NucleusAlgorithm import NucleusAlgorithm
from OPRFEvaluation.OPRFEvaluation import OPRFEvaluation
from OTService.OTService import OTService
from Precomputation.Precomputation import Precomputation

dataEngineering = DataEngineering(CSVParser(), XLSParser())
dataFileNames = ['testFile_512.csv', 'testFile_1024.csv', 'testFile_2048.csv', 'testFile_4096.csv']
data512 = dataEngineering.parse('testFile_512.csv')['Coloana 1']
data1024 = dataEngineering.parse('testFile_1024.csv')['Coloana 1']
data2048 = dataEngineering.parse('testFile_2048.csv')['Coloana 1']
data4096 = dataEngineering.parse('testFile_4096.csv')['Coloana 1']

def generateParameters():
    import NegotiationParameters.Constants
    result = []
    for dataFile in dataFileNames:
        for lambdas in NegotiationParameters.Constants.LAMBDAS:
            for hash1 in NegotiationParameters.Constants.HASHES[lambdas]:
                for prf in NegotiationParameters.Constants.PRFS[lambdas]:
                    for hash2 in NegotiationParameters.Constants.HASH_LIST:
                        for otVariant in NegotiationParameters.Constants.OT_VARIANTS:
                            result.append([dataFile, lambdas, hash1, hash2, prf, otVariant])
    return result


class ParamSender(TestCase):

    @parameterized.parameterized.expand(generateParameters())
    def test_receiverTest(self, dataFile, lambdas, hash1, hash2, prf, otVariant):
        print(str(lambdas) + ' ' + hash1 + ' ' + hash2 + ' ' + prf + ' ' + str(otVariant))

        if dataFile == 'testFile_512.csv':
            data = data512
        elif dataFile == 'testFile_1024.csv':
            data = data1024
        elif dataFile == 'testFile_2048.csv':
            data = data2048
        else:
            data = data4096

        dictParameters = {
            'lambda': lambdas,
            'sigma': 60,
            'm': len(data),
            'w': 100,
            'l1': 1284,
            'l2': 50,
            'hash1': hash1,
            'hash2': hash2,
            'prf': prf,
            'otVariant': otVariant,
        }

        pubKeyServer = RSA.importKey(open(os.path.join("server_rsa_public.pem")).read())
        privKeyServer = RSA.importKey(open(os.path.join("server_rsa_private.pem")).read())

        comSend = ComSend(SocketPool(20))
        comReceive = ComReceive(SocketPool(20))

        transferProtocol = TransferProtocol({'Server IP': Constants.SENDER_ADDRESS, 'Server Port': Constants.SENDER_PORT,
                                             'Client IP': Constants.RECEIVER_ADDRESS, 'Client Port': Constants.RECEIVER_PORT}
                                            , comSend, comReceive)

        negociateParametersUtils = NegotiateParametersUtils()
        negotiateParameters = NegociateParameters(transferProtocol, negociateParametersUtils)
        precomputation = Precomputation()
        otService = OTService(transferProtocol)
        oprfEvaluation = OPRFEvaluation(transferProtocol)

        nucleusAlgorithm = NucleusAlgorithm(data, dictParameters, negotiateParameters, precomputation, otService,
                                            oprfEvaluation)

        transferProtocol.receiveInitiateConnection()
        transferProtocol.sendConfirmationInitiateConnection()
        pubKeyClient = transferProtocol.receiveRSAReceiverPublicKey()
        transferProtocol.sendRSASenderPublicKey(pubKeyServer)
        transferProtocol.receiveIVByRSA(privKeyServer)
        transferProtocol.sendAESKeyByRSA(transferProtocol.aesKey, pubKeyClient)
        nucleusAlgorithm.senderAlgorithmSide()
