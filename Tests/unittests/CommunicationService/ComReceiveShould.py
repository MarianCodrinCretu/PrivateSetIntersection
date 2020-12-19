import pickle
import socket
from unittest import TestCase

from mockito import mock, when, verify, unstub, ANY

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
    aesKey = 'aesKey'
    aesIV = 'aesIV'
    dummyHeadersize = 10

    dummyData = "datadatadatadatadatadatadatadatadatadata"

    def test_receiveData(self):
        flag = 'NoAES'

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        connection = mock(socket.socket)
        address = mock()

        # setup
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        when(socketMock).listen(5)

        when(socketMock).accept().thenReturn((connection, address))
        when(connection).recv(self.dummySizeOfDatagram).thenReturn(b'5')

        when(pickle).loads(ANY).thenReturn(self.dummyData)

        when(socketPool).release(socketMock)

        # execute
        comReceive = ComReceive(socketPool, self.aesKey, self.aesIV)

        result = comReceive.receive(self.dummyIP, self.dummyPort, self.dummyHeadersize, self.dummySizeOfDatagram,
                                    flag=flag)

        # verify

        self.assertEqual(result, self.dummyData)

        # verify
        verify(socketPool).acquire()
        verify(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        verify(socketMock).listen(5)

        verify(socketMock).accept()
        verify(connection, atleast=1).recv(self.dummySizeOfDatagram)

        verify(pickle).loads(ANY)

        verify(socketPool).release(socketMock)

        unstub()

    def test_receiveDataFailsWhenBindingException(self):
        flag = 'NoAES'

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        connection = mock(socket.socket)
        address = mock()

        # setup
        exception = Exception('Binding error')
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).bind((self.dummyIP, int(self.dummyPort))).thenRaise(exception)

        when(pickle).loads(ANY).thenReturn(self.dummyData)

        # execute
        comReceive = ComReceive(socketPool, self.aesKey, self.aesIV)
        with self.assertRaises(Exception) as context:
            comReceive.receive(self.dummyIP, self.dummyPort, self.dummyHeadersize, self.dummySizeOfDatagram, flag=flag)
            self.assertEqual('Binding error', context.exception)

        # verify

        verify(socketPool).acquire()
        verify(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        verify(socketMock, times=0).listen(5)

        verify(socketMock, times=0).accept()
        verify(connection, times=0).recv(self.dummySizeOfDatagram)

        verify(pickle, times=0).loads(ANY)

        verify(socketPool, times=0).release(socketMock)

        unstub()

    def test_receiveDataFailsWhenListeningException(self):
        flag = 'NoAES'

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        connection = mock(socket.socket)
        address = mock()

        # setup
        exception = Exception('Listening error')
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        when(socketMock).listen(5).thenRaise(exception)

        when(pickle).loads(ANY).thenReturn(self.dummyData)

        # execute
        comReceive = ComReceive(socketPool, self.aesKey, self.aesIV)
        with self.assertRaises(Exception) as context:
            comReceive.receive(self.dummyIP, self.dummyPort, self.dummyHeadersize, self.dummySizeOfDatagram, flag=flag)
            self.assertEqual('Listening error', context.exception)

        # verify

        verify(socketPool).acquire()
        verify(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        verify(socketMock).listen(5)

        verify(socketMock, times=0).accept()
        verify(connection, times=0).recv(self.dummySizeOfDatagram)

        verify(pickle, times=0).loads(ANY)

        verify(socketPool, times=0).release(socketMock)

        unstub()

    def test_receiveDataFailsWhenAcceptingException(self):
        flag = 'NoAES'

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        connection = mock(socket.socket)
        address = mock()

        # setup
        exception = Exception('Accepting error')
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        when(socketMock).listen(5)
        when(socketMock).accept().thenRaise(exception)

        when(pickle).loads(ANY).thenReturn(self.dummyData)

        # execute
        comReceive = ComReceive(socketPool, self.aesKey, self.aesIV)
        with self.assertRaises(Exception) as context:
            comReceive.receive(self.dummyIP, self.dummyPort, self.dummyHeadersize, self.dummySizeOfDatagram, flag=flag)
            self.assertEqual('Accepting error', context.exception)

        # verify

        verify(socketPool).acquire()
        verify(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        verify(socketMock).listen(5)

        verify(socketMock).accept()
        verify(connection, times=0).recv(self.dummySizeOfDatagram)

        verify(pickle, times=0).loads(ANY)

        verify(socketPool, times=0).release(socketMock)

        unstub()

    def test_receiveDataFailsWhenRecvException(self):
        flag = 'NoAES'

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        connection = mock(socket.socket)
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
        comReceive = ComReceive(socketPool, self.aesKey, self.aesIV)
        with self.assertRaises(Exception) as context:
            comReceive.receive(self.dummyIP, self.dummyPort, self.dummyHeadersize, self.dummySizeOfDatagram, flag=flag)
            self.assertEqual('Recv error', context.exception)

        # verify

        verify(socketPool).acquire()
        verify(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        verify(socketMock).listen(5)

        verify(socketMock).accept()
        verify(connection, times=1).recv(self.dummySizeOfDatagram)

        verify(pickle, times=0).loads(ANY)

        verify(socketPool, times=0).release(socketMock)

        unstub()

    def test_receiveDataFailsWhenDeserializingException(self):
        flag = 'NoAES'

        socketPool = mock(SocketPool)
        socketMock = mock(socket.socket)
        connection = mock(socket.socket)
        address = mock()

        # setup
        exception = Exception('Load error')
        when(socketPool).acquire().thenReturn(socketMock)
        when(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        when(socketMock).listen(5)
        when(socketMock).accept().thenReturn((connection, address))
        when(connection).recv(self.dummySizeOfDatagram).thenReturn(b'5')
        when(pickle).loads(ANY).thenRaise(exception)

        # execute
        comReceive = ComReceive(socketPool, self.aesKey, self.aesIV)
        with self.assertRaises(Exception) as context:
            comReceive.receive(self.dummyIP, self.dummyPort, self.dummyHeadersize, self.dummySizeOfDatagram, flag=flag)
            self.assertEqual('Load error', context.exception)

        # verify

        verify(socketPool).acquire()
        verify(socketMock).bind((self.dummyIP, int(self.dummyPort)))
        verify(socketMock).listen(5)

        verify(socketMock).accept()
        verify(connection, atleast=1).recv(self.dummySizeOfDatagram)

        verify(pickle, times=0).loads(ANY)

        verify(socketPool, times=0).release(socketMock)

        unstub()
