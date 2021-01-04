import os
from unittest import TestCase
import time


import parameterized
from Crypto.PublicKey import RSA

import Constants
from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol
from NegotiationParameters.NegotiateParameters import NegociateParameters
from NegotiationParameters.NegotiateParametersUtils import NegotiateParametersUtils
from NucleusAlgorithm.NucleusAlgorithm import NucleusAlgorithm
from OPRFEvaluation.OPRFEvaluation import OPRFEvaluation
from OTService.OTService import OTService
from Precomputation.Precomputation import Precomputation

data = ['Vito Corleone', 'Sonny Corleone', 'Michael Corleone', 'Tom Hagen', 'Kay Adams', 'Mary Corleone', 'Apollonia Vitelli-Corleone']

def generateParameters():
    import NegotiationParameters.Constants
    result = []
    for lambdas in NegotiationParameters.Constants.LAMBDAS:
        for hash1 in NegotiationParameters.Constants.HASHES[lambdas]:
            for prf in NegotiationParameters.Constants.PRFS[lambdas]:
                for hash2 in NegotiationParameters.Constants.HASH_LIST:
                    result.append([lambdas, hash1, hash2, prf])
    return result

def writeStatistics(otVariant, hash1, hash2, prf, time):
    if otVariant == '1':
        filex = 'statisticsOt1Faster.txt'
    else:
        filex = 'statisticsOt2Faster.txt'

    with open(filex, 'a') as fileWrite:
        fileWrite.write(hash1+' --- '+hash2+' --- '+prf+' --- '+ str(time))
        fileWrite.write('\n\n')



class ParamTestReceiver(TestCase):

    @parameterized.parameterized.expand(generateParameters())
    def test_receiverTest(self, lambdas, hash1, hash2, prf):

        print(str(lambdas) +' '+hash1+' '+hash2+' '+prf)
        dictParameters = {
            'lambda': lambdas,
            'sigma': 60,
            'm': 64,
            'w': 100,
            'l1': 1284,
            'l2': 50,
            'hash1': hash1,
            'hash2': hash2,
            'prf': prf,
            'otVariant': '1',
        }

        pubKeyClient = RSA.importKey(open(os.path.join("client_rsa_public.pem")).read())
        privKeyClient = RSA.importKey(open(os.path.join("client_rsa_private.pem")).read())

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

        # execute

        transferProtocol.initiateConnection()
        transferProtocol.receiveConfirmationInitiateConnection()
        transferProtocol.sendRSAReceiverPublicKey(pubKeyClient)
        pubKeyServer = transferProtocol.receiveRSASenderPublicKey()
        transferProtocol.sendIVByRSA(transferProtocol.aesIV, pubKeyServer)
        transferProtocol.receiveAESKeyByRSA(privKeyClient)

        nucleusAlgorithm = NucleusAlgorithm(data, dictParameters, negotiateParameters, precomputation, otService,
                                            oprfEvaluation)

        start = time.time()
        result = nucleusAlgorithm.receiverAlgorithmSide()
        end = time.time()

        writeStatistics(dictParameters['otVariant'], dictParameters['hash1'], dictParameters['hash2'], dictParameters['prf'], end-start)

        print(result)

        self.assertTrue(len(result)==2)
        for element in ['Vito Corleone', 'Tom Hagen']:
            self.assertTrue(element in result)
