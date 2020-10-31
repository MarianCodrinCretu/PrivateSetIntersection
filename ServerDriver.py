import Constants
import time

from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol

transferProtocol = TransferProtocol(SocketPool(20), {'Server IP': Constants.SENDER_ADDRESS, 'Server Port': Constants.SENDER_PORT})

print(transferProtocol.receiveNegotiateParameters())

print('OT VALUES ' + str(transferProtocol.receiveOT()))

print(transferProtocol.receiveKey())

transferProtocol.sendPsiValues([[i for i in range(10)]for j in range(10)])
