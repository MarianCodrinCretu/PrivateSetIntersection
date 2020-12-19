import pickle
import socket
from unittest import TestCase

from mockito import mock, when, verify, unstub

import Constants
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool


class ComSendShould(TestCase):
    _connectionParams = {'Server IP': Constants.SENDER_ADDRESS,
                         'Server Port': Constants.SENDER_PORT,
                         'Client IP': Constants.RECEIVER_ADDRESS,
                         'Client Port': Constants.RECEIVER_PORT}

    dummyId = _connectionParams['Server IP']
    dummyPort = int(_connectionParams['Server Port'])
    aesKey = 'aesKey'
    aesIV = 'aesIV'
    dummyHeadersize = 10

    dummyData = "datadatadatadatadatadatadatadatadatadata"

    def test_sendData(self):
        flag = 'NoAES'

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)

        # setup
        when(pickle).dumps(self.dummyData).thenReturn(b'123')
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).connect((self.dummyId, self.dummyPort))

        data = bytes(f"{len(b'123'):<{self.dummyHeadersize}}", 'utf-8') + b'123'

        when(socketMock).send(data)
        when(socketPool).release(socketMock)

        # execute
        comSend = ComSend(socketPool, self.aesKey, self.aesIV)

        comSend.send(self.dummyData, self.dummyId, self.dummyPort, self.dummyHeadersize, flag=flag)

        # verify
        verifyData = self.dummyData
        verify(pickle).dumps(verifyData)
        verify(socketPool).acquire()
        verify(socketMock).connect((self.dummyId, self.dummyPort))

        verifyData = bytes(f"{len(b'123'):<{self.dummyHeadersize}}", 'utf-8') + b'123'

        verify(socketMock).send(verifyData)
        verify(socketPool).release(socketMock)

        unstub()

    def test_sendDataFailedPickleError(self):
        flag = 'NoAES'

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)

        # setup
        exception = Exception('Pickle dumping error')
        when(pickle).dumps(self.dummyData).thenRaise(exception)

        # execute
        comSend = ComSend(socketPool, self.aesKey, self.aesIV)
        with self.assertRaises(Exception) as context:
            comSend.send(self.dummyData, self.dummyId, self.dummyPort, self.dummyHeadersize, flag=flag)

            self.assertTrue('Pickle dumping error' in context.exception)

        # verify
        verifyData = self.dummyData
        verify(pickle).dumps(verifyData)
        verify(socketPool, times=0).acquire()
        verify(socketMock, times=0).connect((self.dummyId, self.dummyPort))

        verifyData = bytes(f"{len(b'123'):<{self.dummyHeadersize}}", 'utf-8') + b'123'

        verify(socketMock, times=0).send(verifyData)
        verify(socketPool, times=0).release(socketMock)

        unstub()

    def test_sendDataConnectError(self):
        flag = 'NoAES'

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)

        # setup
        exception = Exception('Connection refused error')
        when(pickle).dumps(self.dummyData).thenReturn(b'123')
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).connect((self.dummyId, self.dummyPort)).thenRaise(exception)

        # execute
        comSend = ComSend(socketPool, self.aesKey, self.aesIV)
        with self.assertRaises(Exception) as context:
            comSend.send(self.dummyData, self.dummyId, self.dummyPort, self.dummyHeadersize, flag=flag)

            self.assertTrue('Connection refused error' in context.exception)

        # verify
        verifyData = self.dummyData
        verify(pickle).dumps(verifyData)
        verify(socketPool).acquire()
        verify(socketMock).connect((self.dummyId, self.dummyPort))

        verifyData = bytes(f"{len(b'123'):<{self.dummyHeadersize}}", 'utf-8') + b'123'

        verify(socketMock, times=0).send(verifyData)
        verify(socketPool, times=0).release(socketMock)

        unstub()

    def test_sendDataSendingError(self):
        flag = 'NoAES'

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)

        # setup
        exception = Exception('Sending error')
        when(pickle).dumps(self.dummyData).thenReturn(b'123')
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).connect((self.dummyId, self.dummyPort))
        data = bytes(f"{len(b'123'):<{self.dummyHeadersize}}", 'utf-8') + b'123'

        when(socketMock).send(data).thenRaise(exception)
        when(socketPool).release(socketMock)

        # execute
        comSend = ComSend(socketPool, self.aesKey, self.aesIV)
        with self.assertRaises(Exception) as context:
            comSend.send(self.dummyData, self.dummyId, self.dummyPort, self.dummyHeadersize, flag=flag)

            self.assertTrue('Connection refused error' in context.exception)

        # verify
        verifyData = self.dummyData
        verify(pickle).dumps(verifyData)
        verify(socketPool).acquire()
        verify(socketMock).connect((self.dummyId, self.dummyPort))

        verifyData = bytes(f"{len(b'123'):<{self.dummyHeadersize}}", 'utf-8') + b'123'

        verify(socketMock).send(verifyData)
        verify(socketPool, times=0).release(socketMock)

        unstub()
