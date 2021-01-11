import random
import string
from unittest import TestCase

from parameterized import parameterized


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def generate_data(sizeOfData, lengthOfWord=16):
    return [get_random_string(lengthOfWord) for _ in range(sizeOfData)]

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


class TestSender(TestCase):

    @parameterized.expand([[10], [25], [50], [100], [200], [500], [1000], [2000], [5000], [10000]])
    def test_senderTest(self, size):
        data = generate_data(size)
        if size<64:
            m=64
        else:
            m=size
        dictParameters = {
            'lambda': 128,
            'sigma': 60,
            'm': m,
            'w': 633,
            'l1': 1284,
            'l2': 50,
            'hash1': 'SHA256',
            'hash2': 'MD5',
            'prf': 'AES',
            'otVariant': '1',
            'lenDataset': len(data)
        }

        comSend = ComSend(SocketPool(20))
        comReceive = ComReceive(SocketPool(20))

        transferProtocol = TransferProtocol({'Server IP': Constants.SENDER_ADDRESS, 'Server Port': Constants.SENDER_PORT,
                                             'Client IP': Constants.RECEIVER_ADDRESS, 'Client Port': Constants.RECEIVER_PORT}
                                            , comSend, comReceive, "Thats my Kung Fu", "ABCDE FG HIJK LM")

        negociateParametersUtils = NegotiateParametersUtils()
        negotiateParameters = NegociateParameters(transferProtocol, negociateParametersUtils)
        precomputation = Precomputation()
        otService = OTService(transferProtocol)
        oprfEvaluation = OPRFEvaluation(transferProtocol)
        nucleusAlgorithm = NucleusAlgorithm(data, dictParameters, negotiateParameters, precomputation, otService,
                                            oprfEvaluation)

        nucleusAlgorithm.senderAlgorithmSide()
