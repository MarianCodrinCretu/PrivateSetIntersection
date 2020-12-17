import Constants
from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol
from Hash.HashBlake2b import HashBlake2b
from Hash.HashMd5 import HashMd5
from Hash.HashSha1 import HashSha1
from Hash.HashSha256 import HashSha256
from NegotiationParameters.NegotiateParameters import NegociateParameters
from NegotiationParameters.NegotiateParametersUtils import NegotiateParametersUtils
from NucleusAlgorithm.NucleusAlgorithm import NucleusAlgorithm
from OPRFEvaluation.OPRFEvaluation import OPRFEvaluation
from OTService.OTService import OTService
from PRF.OPRF import computeOPrfValue
from Precomputation.Precomputation import Precomputation

data = ['Marian', 'Andrei', 'Alexandra', 'Catalina', 'Ana-Maria']


def generateDictFunctions():
    return {
        'MD5': HashMd5(1).generate,
        'SHA1': HashSha1(1).generate,
        'SHA256': HashSha256(1).generate,
        'BLAKE2B': HashBlake2b(1).generate,
        'FK': computeOPrfValue,
    }

dictParameters = {
    'lambda': 128,
    'sigma': 60,
    'm': 1,
    'w': 100,
    'l1': 256,
    'l2': 50,
    'hash1': 'MD5',
    'hash2': 'SHA256',
    'prf': 'AES',
    'otVariant': '1',
    'lenDataset': len(data)
}

dictFunc = generateDictFunctions()
comSend = ComSend(SocketPool(20), "Thats my Kung Fu", "ABCDE FG HIJK LM")
comReceive = ComReceive(SocketPool(20), "Thats my Kung Fu", "ABCDE FG HIJK LM")

transferProtocol = TransferProtocol({'Server IP': Constants.SENDER_ADDRESS, 'Server Port': Constants.SENDER_PORT, 'Client IP':Constants.RECEIVER_ADDRESS, 'Client Port':Constants.RECEIVER_PORT}
                                    , comSend, comReceive)

negociateParametersUtils = NegotiateParametersUtils()
negotiateParameters =  NegociateParameters(transferProtocol, negociateParametersUtils)
precomputation= Precomputation(dictFunc)
otService=OTService(transferProtocol)
oprfEvaluation=OPRFEvaluation(transferProtocol, dictFunc)
nucleusAlgorithm = NucleusAlgorithm(data, dictParameters, negotiateParameters, precomputation, otService, oprfEvaluation )

nucleusAlgorithm.senderAlgorithmSide()