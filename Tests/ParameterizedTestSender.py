

import os
from unittest import TestCase

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

data = ['Marian', 'Adrian Iftene', 'FLT', 'Radu Ionicioiu']

def generateParameters():
    import NegotiationParameters.Constants
    result = []
    for lambdas in NegotiationParameters.Constants.LAMBDAS:
        for hash1 in NegotiationParameters.Constants.HASHES[lambdas]:
            for prf in NegotiationParameters.Constants.PRFS[lambdas]:
                for hash2 in NegotiationParameters.Constants.HASH_LIST:
                    result.append([lambdas, hash1, hash2, prf])
    return result


class ParamSender(TestCase):

    @parameterized.parameterized.expand(generateParameters())
    def test_receiverTest(self, lambdas, hash1, hash2, prf):
        print(str(lambdas) + ' ' + hash1 + ' ' + hash2 + ' ' + prf)
        dictParameters = {
            'lambda': lambdas,
            'sigma': 60,
            'm': 64,
            'w': 487,
            'l1': 1284,
            'l2': 50,
            'hash1': hash1,
            'hash2': hash2,
            'prf': prf,
            'otVariant': '1',
            'lenDataset': len(data)
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
