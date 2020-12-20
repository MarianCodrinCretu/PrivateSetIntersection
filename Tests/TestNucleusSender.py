import Constants
from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol
from Hash.HashBlake2b import HashBlake2b
from Hash.HashMd5 import HashMd5
from Hash.HashSha1 import HashSha1
from Hash.HashSha256 import HashSha256
from Hash.HashSha384 import HashSha384
from Hash.HashSha3_256 import HashSha3_256
from Hash.Sha3_384 import HashSha3_384
from NegotiationParameters.NegotiateParameters import NegociateParameters
from NegotiationParameters.NegotiateParametersUtils import NegotiateParametersUtils
from NucleusAlgorithm.NucleusAlgorithm import NucleusAlgorithm
from OPRFEvaluation.OPRFEvaluation import OPRFEvaluation
from OTService.OTService import OTService
from PRF.OPRF import computeOPrfValue
from Precomputation.Precomputation import Precomputation

data = ['Marian']


dictParameters = {
    'lambda': 128,
    'sigma': 60,
    'm': 64,
    'w': 633,
    'l1': 1284,
    'l2': 50,
    'hash1': 'BLAKE2B_32',
    'hash2': 'BLAKE2B_32',
    'prf': 'AES',
    'otVariant': '1',
    'lenDataset': len(data)
}

comSend = ComSend(SocketPool(20))
comReceive = ComReceive(SocketPool(20))

transferProtocol = TransferProtocol({'Server IP': Constants.SENDER_ADDRESS, 'Server Port': Constants.SENDER_PORT, 'Client IP':Constants.RECEIVER_ADDRESS, 'Client Port':Constants.RECEIVER_PORT}
                                    , comSend, comReceive, "Thats my Kung Fu", "ABCDE FG HIJK LM")

negociateParametersUtils = NegotiateParametersUtils()
negotiateParameters =  NegociateParameters(transferProtocol, negociateParametersUtils)
precomputation= Precomputation()
otService=OTService(transferProtocol)
oprfEvaluation=OPRFEvaluation(transferProtocol)
nucleusAlgorithm = NucleusAlgorithm(data, dictParameters, negotiateParameters, precomputation, otService, oprfEvaluation )

nucleusAlgorithm.senderAlgorithmSide()