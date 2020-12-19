import pickle
import socket
from unittest import TestCase

from Crypto.Cipher import AES
from mockito import mock, when, verify, unstub, ANY
from parameterized import parameterized

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
    key = '1111111111111111'
    aesKey = key.encode('utf8')
    aesIV = key.encode('utf8')

    cipher = AES.new(aesKey, AES.MODE_OFB, aesIV)

    dummyHeadersize = 10

    dummyData = "datadatadatadatadatadatadatadatadatadata"

    @parameterized.expand([['NoAES'], ['AES']])
    def test_sendData(self, flag):

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        aesMock = mock(AES.new(self.aesKey, AES.MODE_OFB, self.aesIV))

        # setup
        data = b'123'
        copyData = data

        when(pickle).dumps(self.dummyData).thenReturn(data)
        when(aesMock).encrypt(data).thenReturn(data)
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).connect((self.dummyId, self.dummyPort))

        data = bytes(f"{len(data):<{self.dummyHeadersize}}", 'utf-8') + data

        when(socketMock).send(data)
        when(socketPool).release(socketMock)

        # execute
        comSend = ComSend(socketPool)

        comSend.send(self.dummyData, self.dummyId, self.dummyPort, self.dummyHeadersize, aesCipher=aesMock, flag=flag)

        # verify
        verifyData = self.dummyData
        verify(pickle).dumps(verifyData)
        if flag == 'NoAES':
            verify(aesMock, times=0).encrypt(copyData)
        else:
            verify(aesMock, times=1).encrypt(copyData)

        verify(socketPool).acquire()
        verify(socketMock).connect((self.dummyId, self.dummyPort))

        verifyData = bytes(f"{len(b'123'):<{self.dummyHeadersize}}", 'utf-8') + b'123'

        verify(socketMock).send(verifyData)
        verify(socketPool).release(socketMock)

        unstub()

    @parameterized.expand([['NoAES'], ['AES']])
    def test_sendDataFailedPickleError(self, flag):

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        aesMock = mock(AES.new(self.aesKey, AES.MODE_OFB, self.aesIV))

        # setup
        exception = Exception('Pickle dumping error')
        when(pickle).dumps(self.dummyData).thenRaise(exception)

        # execute
        comSend = ComSend(socketPool)
        with self.assertRaises(Exception) as context:
            comSend.send(self.dummyData, self.dummyId, self.dummyPort, self.dummyHeadersize, aesCipher=aesMock,
                         flag=flag)

            self.assertTrue(str(exception) in context.exception)

        # verify
        verifyData = self.dummyData
        verify(pickle).dumps(verifyData)
        verify(aesMock, times=0).encrypt(ANY)
        verify(socketPool, times=0).acquire()
        verify(socketMock, times=0).connect((self.dummyId, self.dummyPort))

        verifyData = bytes(f"{len(b'123'):<{self.dummyHeadersize}}", 'utf-8') + b'123'

        verify(socketMock, times=0).send(ANY)
        verify(socketPool, times=0).release(ANY)

        unstub()

    @parameterized.expand([['NoAES'], ['AES']])
    def test_sendDataConnectError(self, flag):

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        aesMock = mock(AES.new(self.aesKey, AES.MODE_OFB, self.aesIV))

        # setup
        data = b'123'
        copyData = data

        exception = Exception('Connection refused error')
        when(pickle).dumps(self.dummyData).thenReturn(data)
        when(aesMock).encrypt(data).thenReturn(data)
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).connect((self.dummyId, self.dummyPort)).thenRaise(exception)

        # execute
        comSend = ComSend(socketPool)
        with self.assertRaises(Exception) as context:
            comSend.send(self.dummyData, self.dummyId, self.dummyPort, self.dummyHeadersize, flag=flag,
                         aesCipher=aesMock)

            self.assertTrue(str(exception) in context.exception)

        # verify
        verifyData = self.dummyData
        verify(pickle).dumps(verifyData)
        if flag == 'NoAES':
            verify(aesMock, times=0).encrypt(copyData)
        else:
            verify(aesMock, times=1).encrypt(copyData)
        verify(socketPool).acquire()
        verify(socketMock).connect((self.dummyId, self.dummyPort))

        verifyData = bytes(f"{len(b'123'):<{self.dummyHeadersize}}", 'utf-8') + b'123'

        verify(socketMock, times=0).send(verifyData)
        verify(socketPool, times=0).release(socketMock)

        unstub()

    @parameterized.expand([['NoAES'], ['AES']])
    def test_sendDataSendingError(self, flag):
        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        aesMock = mock(AES.new(self.aesKey, AES.MODE_OFB, self.aesIV))

        # setup
        data = b'123'
        copyData = data

        exception = Exception('Sending error')
        when(pickle).dumps(self.dummyData).thenReturn(b'123')
        when(aesMock).encrypt(data).thenReturn(data)
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).connect((self.dummyId, self.dummyPort))
        data = bytes(f"{len(b'123'):<{self.dummyHeadersize}}", 'utf-8') + b'123'

        when(socketMock).send(data).thenRaise(exception)
        when(socketPool).release(socketMock)

        # execute
        comSend = ComSend(socketPool)
        with self.assertRaises(Exception) as context:
            comSend.send(self.dummyData, self.dummyId, self.dummyPort, self.dummyHeadersize, aesCipher=aesMock,
                         flag=flag)

            self.assertTrue(str(exception) in context.exception)

        # verify
        verifyData = self.dummyData
        verify(pickle).dumps(verifyData)
        if flag == 'NoAES':
            verify(aesMock, times=0).encrypt(copyData)
        else:
            verify(aesMock, times=1).encrypt(copyData)
        verify(socketPool).acquire()
        verify(socketMock).connect((self.dummyId, self.dummyPort))

        verifyData = bytes(f"{len(b'123'):<{self.dummyHeadersize}}", 'utf-8') + b'123'

        verify(socketMock).send(verifyData)
        verify(socketPool, times=0).release(socketMock)

        unstub()

    def test_sendDataFailedAESError(self):

        flag = 'AES'

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        aesMock = mock(AES.new(self.aesKey, AES.MODE_OFB, self.aesIV))

        # setup
        exception = Exception('AES Encrypting error')
        data = b'123'
        copyData = data

        when(pickle).dumps(self.dummyData).thenReturn(data)
        when(aesMock).encrypt(data).thenRaise(exception)

        # execute
        comSend = ComSend(socketPool)
        with self.assertRaises(Exception) as context:
            comSend.send(self.dummyData, self.dummyId, self.dummyPort, self.dummyHeadersize, aesCipher=aesMock,
                         flag=flag)

            self.assertTrue(str(exception) in context.exception)

        # verify
        verifyData = self.dummyData
        verify(pickle).dumps(verifyData)
        verify(aesMock, times=1).encrypt(copyData)
        verify(socketPool, times=0).acquire()
        verify(socketMock, times=0).connect((self.dummyId, self.dummyPort))

        verify(socketMock, times=0).send(ANY)
        verify(socketPool, times=0).release(ANY)

        unstub()
