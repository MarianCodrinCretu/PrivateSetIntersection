import Constants
import time
from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol

transferProtocol = TransferProtocol(SocketPool(20), {'Server IP': Constants.SENDER_ADDRESS, 'Server Port': Constants.SENDER_PORT, 'Client IP':Constants.RECEIVER_ADDRESS, 'Client Port':Constants.RECEIVER_PORT})

#
transferProtocol.sendNegotiateParameters({'message': 'I love Quantum Computing', 'message2': 'I love Superposition and Entanglement', 'planck':6.61e-2})

transferProtocol.sendOT([[i for i in range(10)]for j in range(10)])

transferProtocol.sendPRFKey("Cretu Marian-Codrin")

print('PSI VALUES ' + str( transferProtocol.receivePsiValues()))
