from unittest import TestCase
from unittest.mock import MagicMock, Mock
from unittest.mock import patch
from unittest.mock import create_autospec

from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool

import socket


def mockFailConnection():
    raise ConnectionRefusedError

def mockPassConnection():
    pass

socketPool = Mock()
socketMock = Mock()

#@patch("CommunicationService.SocketPool", new=socketPool)
class ComSendShould(TestCase):

    def test_sendNormallyIfConnectionToServerIsOkay(self):

        #setup
        socketPoolEngine = create_autospec(SocketPool)
        socketPoolEngine.acquire.return_value = socketMock

        socketMock.send.return_value = None

        comSend = ComSend(socketPoolEngine)
        dummyPort = 1548
        dummyHeaderSize = 100
        comSend.send("toBeSent", "ip", dummyPort, dummyHeaderSize)

    def test_failIfConnectionToServerIsNotEstablished(self):

        #setup
        with patch('socket.socket.send') as socketMockToTest:
            socketMockToTest.side_effect = ConnectionRefusedError()
            socketPoolEngine = create_autospec(SocketPool)
            socketPoolEngine.acquire.return_value = socketMockToTest

            comSend = ComSend(socketPoolEngine)
            dummyPort = 1548
            dummyHeaderSize = 100
            comSend.send("toBeSent", "ip", dummyPort, dummyHeaderSize)
            self.assertRaises(ConnectionRefusedError)
