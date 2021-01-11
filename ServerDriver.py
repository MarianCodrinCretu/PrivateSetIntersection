import Constants
import time

from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol

comSend = ComSend(SocketPool(20), "Thats my Kung Fu", "ABCDE FG HIJK LM")
comReceive = ComReceive(SocketPool(20), "Thats my Kung Fu", "ABCDE FG HIJK LM")

transferProtocol = TransferProtocol({'Server IP': Constants.SENDER_ADDRESS, 'Server Port': Constants.SENDER_PORT, 'Client IP':Constants.RECEIVER_ADDRESS, 'Client Port':Constants.RECEIVER_PORT}
                                    , comSend, comReceive)

print(transferProtocol.receiveInitiateConnection())

transferProtocol.sendConfirmationInitiateConnection()

print(transferProtocol.receiveNegotiateParameters())

print('OT VALUES ' + str(transferProtocol.receiveOT()))

print(transferProtocol.receiveKey())

transferProtocol.sendPsiValues([[i for i in range(10)]for j in range(10)])
