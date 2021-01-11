import Constants
import time

from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol
from InitiateCommunication.InitiateCommunication import InitiateCommunication

comSend = ComSend(SocketPool(20), "Thats my Kung Fu", "ABCDE FG HIJK LM")
comReceive = ComReceive(SocketPool(20), "Thats my Kung Fu", "ABCDE FG HIJK LM")

transferProtocol = TransferProtocol({'Server IP': Constants.SENDER_ADDRESS, 'Server Port': Constants.SENDER_PORT, 'Client IP':Constants.RECEIVER_ADDRESS, 'Client Port':Constants.RECEIVER_PORT}
                                    , comSend, comReceive)

time.sleep(0.2)
initiateCommunication = InitiateCommunication(transferProtocol)
initiateCommunication.initiateConnection()

print(initiateCommunication.receiveConfirmationInitiateConnection())