import pickle
import socket
from unittest import TestCase

from Crypto.Cipher import AES
from mockito import mock, when, verify, unstub, ANY
from parameterized import parameterized

import Constants
from CommunicationService.ComReceive import ComReceive
from CommunicationService.SocketPool import SocketPool


class ComReceiveShould(TestCase):
    _connectionParams = {'Server IP': Constants.SENDER_ADDRESS,
                         'Server Port': Constants.SENDER_PORT,
                         'Client IP': Constants.RECEIVER_ADDRESS,
                         'Client Port': Constants.RECEIVER_PORT}

    dummyIP = _connectionParams['Server IP']
    dummyPort = int(_connectionParams['Server Port'])
    dummySizeOfDatagram = 16
    key = '1111111111111111'
    aesKey = key.encode('utf8')
    aesIV = key.encode('utf8')

    cipher = AES.new(aesKey, AES.MODE_OFB, aesIV)

    dummyHeadersize = 10

    dummyData = "datadatadatadatadatadatadatadatadatadata"

    @parameterized.expand([['NoAES'], ['AES']])
    def test_receiveData(self, flag):

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        connection = mock(socket.socket)
        aesMock = mock(AES.new(self.aesKey, AES.MODE_OFB, self.aesIV))

        address = mock()

        # setup
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        when(socketMock).listen(5)

        when(socketMock).accept().thenReturn((connection, address))
        when(connection).recv(self.dummySizeOfDatagram).thenReturn(b'5')
        result = b'55555'
        copyResult = result
        if flag == 'AES':
            when(aesMock).decrypt(result).thenReturn(result)
        when(pickle).loads(result).thenReturn(self.dummyData)

        when(socketPool).release(socketMock)

        # execute
        comReceive = ComReceive(socketPool)

        result = comReceive.receive(self.dummyIP, self.dummyPort, self.dummyHeadersize, aesMock,
                                    self.dummySizeOfDatagram,
                                    flag=flag)

        # verify

        self.assertEqual(result, self.dummyData)

        # verify
        verify(socketPool).acquire()
        verify(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        verify(socketMock).listen(5)

        verify(socketMock).accept()
        verify(connection, atleast=1).recv(self.dummySizeOfDatagram)
        if flag == 'AES':
            verify(aesMock).decrypt(copyResult)
        verify(pickle).loads(copyResult)

        verify(socketPool).release(socketMock)

        unstub()

    @parameterized.expand([['NoAES'], ['AES']])
    def test_receiveDataFailsWhenBindingException(self, flag):

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        connection = mock(socket.socket)
        aesMock = mock(AES.new(self.aesKey, AES.MODE_OFB, self.aesIV))
        address = mock()

        # setup
        exception = Exception('Binding error')
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).bind((self.dummyIP, int(self.dummyPort))).thenRaise(exception)

        when(pickle).loads(ANY).thenReturn(self.dummyData)

        # execute
        comReceive = ComReceive(socketPool)
        with self.assertRaises(Exception) as context:
            comReceive.receive(self.dummyIP, self.dummyPort, self.dummyHeadersize, aesMock, self.dummySizeOfDatagram,
                               flag=flag)
            self.assertEqual(str(exception), context.exception)

        # verify

        verify(socketPool).acquire()
        verify(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        verify(socketMock, times=0).listen(5)

        verify(socketMock, times=0).accept()
        verify(connection, times=0).recv(self.dummySizeOfDatagram)

        verify(aesMock, times=0).decrypt(ANY)
        verify(pickle, times=0).loads(ANY)

        verify(socketPool, times=0).release(socketMock)

        unstub()

    @parameterized.expand([['NoAES'], ['AES']])
    def test_receiveDataFailsWhenListeningException(self, flag):

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        connection = mock(socket.socket)
        aesMock = mock(AES.new(self.aesKey, AES.MODE_OFB, self.aesIV))
        address = mock()

        # setup
        exception = Exception('Listening error')
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        when(socketMock).listen(5).thenRaise(exception)

        when(pickle).loads(ANY).thenReturn(self.dummyData)

        # execute
        comReceive = ComReceive(socketPool)
        with self.assertRaises(Exception) as context:
            comReceive.receive(self.dummyIP, self.dummyPort, self.dummyHeadersize, aesMock, self.dummySizeOfDatagram,
                               flag=flag)
            self.assertEqual(str(exception), context.exception)

        # verify

        verify(socketPool).acquire()
        verify(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        verify(socketMock).listen(5)

        verify(socketMock, times=0).accept()
        verify(connection, times=0).recv(self.dummySizeOfDatagram)

        verify(aesMock, times=0).decrypt(ANY)
        verify(pickle, times=0).loads(ANY)

        verify(socketPool, times=0).release(socketMock)

        unstub()

    @parameterized.expand([['NoAES'], ['AES']])
    def test_receiveDataFailsWhenAcceptingException(self, flag):

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        connection = mock(socket.socket)
        aesMock = mock(AES.new(self.aesKey, AES.MODE_OFB, self.aesIV))
        address = mock()

        # setup
        exception = Exception('Accepting error')
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        when(socketMock).listen(5)
        when(socketMock).accept().thenRaise(exception)

        when(pickle).loads(ANY).thenReturn(self.dummyData)

        # execute
        comReceive = ComReceive(socketPool)
        with self.assertRaises(Exception) as context:
            comReceive.receive(self.dummyIP, self.dummyPort, self.dummyHeadersize, aesMock, self.dummySizeOfDatagram,
                               flag=flag)
            self.assertEqual(str(exception), context.exception)

        # verify

        verify(socketPool).acquire()
        verify(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        verify(socketMock).listen(5)

        verify(socketMock).accept()
        verify(connection, times=0).recv(self.dummySizeOfDatagram)

        if flag == 'AES':
            verify(aesMock, times=0).decrypt(ANY)
        verify(pickle, times=0).loads(ANY)

        verify(socketPool, times=0).release(socketMock)

        unstub()

    @parameterized.expand([['NoAES'], ['AES']])
    def test_receiveDataFailsWhenRecvException(self, flag):

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        connection = mock(socket.socket)
        aesMock = mock(AES.new(self.aesKey, AES.MODE_OFB, self.aesIV))
        address = mock()

        # setup
        exception = Exception('Recv error')
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        when(socketMock).listen(5)
        when(socketMock).accept().thenReturn((connection, address))
        when(connection).recv(self.dummySizeOfDatagram).thenRaise(exception)
        when(pickle).loads(ANY).thenReturn(self.dummyData)

        # execute
        comReceive = ComReceive(socketPool)
        with self.assertRaises(Exception) as context:
            comReceive.receive(self.dummyIP, self.dummyPort, self.dummyHeadersize, aesMock, self.dummySizeOfDatagram,
                               flag=flag)
            self.assertEqual(str(exception), context.exception)

        # verify

        verify(socketPool).acquire()
        verify(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        verify(socketMock).listen(5)

        verify(socketMock).accept()
        verify(connection, times=1).recv(self.dummySizeOfDatagram)

        if flag == 'AES':
            verify(aesMock, times=0).decrypt(ANY)
        verify(pickle, times=0).loads(ANY)

        verify(socketPool, times=0).release(socketMock)

        unstub()

    @parameterized.expand([['NoAES'], ['AES']])
    def test_receiveDataFailsWhenDeserializingException(self, flag):
        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        connection = mock(socket.socket)
        aesMock = mock(AES.new(self.aesKey, AES.MODE_OFB, self.aesIV))
        address = mock()

        # setup
        exception = Exception('Load error')
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        when(socketMock).listen(5)
        when(socketMock).accept().thenReturn((connection, address))
        when(connection).recv(self.dummySizeOfDatagram).thenReturn(b'5')
        result = b'55555'
        copyResult = result

        if flag == 'AES':
            when(aesMock).decrypt(result).thenReturn(result)

        when(pickle).loads(result).thenRaise(exception)

        # execute
        comReceive = ComReceive(socketPool)

        with self.assertRaises(Exception) as context:
            comReceive.receive(self.dummyIP, self.dummyPort, self.dummyHeadersize, aesMock, self.dummySizeOfDatagram,
                               flag=flag)
            self.assertEqual(str(exception), context.exception)

        # verify

        verify(socketPool).acquire()
        verify(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        verify(socketMock).listen(5)

        verify(socketMock).accept()
        verify(connection, atleast=1).recv(self.dummySizeOfDatagram)

        if flag == 'AES':
            # mocking not working properly with aspectlib (times=0 is mandatory);
            # if one of the methods inside the aspect fail, then
            # the mock will not be registered, but the behaviour of mocks is correct
            verify(aesMock, times=0).decrypt(copyResult)

        verify(pickle, times=0).loads(copyResult)

        verify(socketPool, times=0).release(socketMock)

        unstub()

    def test_receiveDataFailsWhenAESDecryptingException(self):

        flag = 'AES'
        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        connection = mock(socket.socket)
        aesMock = mock(AES.new(self.aesKey, AES.MODE_OFB, self.aesIV))
        address = mock()

        # setup
        exception = Exception('AES Decrypting error')
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        when(socketMock).listen(5)
        when(socketMock).accept().thenReturn((connection, address))
        when(connection).recv(self.dummySizeOfDatagram).thenReturn(b'5')
        result = b'55555'
        copyResult = result

        if flag == 'AES':
            when(aesMock).decrypt(result).thenRaise(exception)

        when(pickle).loads(result).thenRaise(result)

        # execute
        comReceive = ComReceive(socketPool)

        with self.assertRaises(Exception) as context:
            comReceive.receive(self.dummyIP, self.dummyPort, self.dummyHeadersize, aesMock, self.dummySizeOfDatagram,
                               flag=flag)
            self.assertEqual(str(exception), context.exception)

        # verify

        verify(socketPool).acquire()
        verify(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        verify(socketMock).listen(5)

        verify(socketMock).accept()
        verify(connection, atleast=1).recv(self.dummySizeOfDatagram)

        if flag == 'AES':
            verify(aesMock, times=0).decrypt(copyResult)

        verify(pickle, times=0).loads(copyResult)

        verify(socketPool, times=0).release(socketMock)

        unstub()
