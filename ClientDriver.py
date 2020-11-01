import Constants
import time

from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol

comSend = ComSend(SocketPool(20))
comReceive = ComReceive(SocketPool(20))

transferProtocol = TransferProtocol({'Server IP': Constants.SENDER_ADDRESS, 'Server Port': Constants.SENDER_PORT, 'Client IP':Constants.RECEIVER_ADDRESS, 'Client Port':Constants.RECEIVER_PORT}
                                    , comSend, comReceive)

transferProtocol.initiateConnection()

print(transferProtocol.receiveConfirmationInitiateConnection())

transferProtocol.sendNegotiateParameters({'message': 'I love Quantum Computing', 'message2': 'I love Superposition and Entanglement', 'planck':6.61e-2})

time.sleep(0.5)
transferProtocol.sendOT([[i for i in range(10)]for j in range(10)])

time.sleep(0.5)

transferProtocol.sendPRFKey("Cretu Marian-Codrin")

print('PSI VALUES ' + str( transferProtocol.receivePsiValues()))
