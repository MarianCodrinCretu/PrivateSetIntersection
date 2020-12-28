import os

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

data = ['Andrada', 'Andrei', 'Stefania', 'Marian', 'Anca', 'Sorin Iftene', 'Adrian Iftene', 'FLT']

dictParameters = {
    'lambda': 128,
    'sigma': 60,
    'm': 64,
    'w': 633,
    'l1': 1284,
    'l2': 50,
    'hash1': 'SHA256',
    'hash2': 'MD5',
    'prf': 'AES',
    'otVariant': '1',
    'lenDataset': len(data)
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

print(nucleusAlgorithm.receiverAlgorithmSide())
