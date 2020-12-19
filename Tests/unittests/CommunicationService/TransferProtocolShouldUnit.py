from unittest import TestCase

from mockito import when, mock, unstub, verify
from mockito.matchers import any
from parameterized import parameterized

import Constants
from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.TransferProtocol import TransferProtocol
from CryptoUtils import CryptoUtils


class TransferProtocolShouldUnit(TestCase):
    # mocking
    _connectionParams = {'Server IP': Constants.SENDER_ADDRESS,
                         'Server Port': Constants.SENDER_PORT,
                         'Client IP': Constants.RECEIVER_ADDRESS,
                         'Client Port': Constants.RECEIVER_PORT}

    comSend = None
    comReceive = None

    def parametersMapper(self, index):
        if index == 1:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   [], str, "Connection attempting!", 10, 'NoAES'
        if index == 2:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), \
                   [], str, "Received connection attempting! All ok!", 10, 'NoAES'
        if index == 3:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   [{'message': 'I love Quantum Computing', 'message2': 'I love Superposition and Entanglement',
                     'planck': 6.61e-2}], dict, {'message': 'I love Quantum Computing',
                                                 'message2': 'I love Superposition and Entanglement',
                                                 'planck': 6.61e-2}, 10, None
        if index == 4:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   [[[i for i in range(10)] for j in range(10)]], list, [[i for i in range(10)] for j in
                                                                         range(10)], 10, None
        if index == 5:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   ["keykeykeykeykey"], str, "keykeykeykeykey", 10, None
        if index == 6:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), \
                   [[[i for i in range(10)] for j in range(10)]], list, [[i for i in range(10)] for j in range(10)], \
                   100, None
        if index == 7:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), ['pubKeyClient'], str, 'pubKeyClient', \
                   50, 'NoAES'
        if index == 8:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), ['pubKeyServer'], str, 'pubKeyServer', \
                   50, 'NoAES'
        if index == 10:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), ['pubKeyServer', 'aesIV'], str, 'aesIV', 10, 'NoAES'
        if index == 9:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), ['pubKeyClient', 'aesKey'], str, 'aesKey', 10, 'NoAES'
        if index == 11:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), \
                   [{'message': 'I love Quantum Computing', 'message2': 'I love Superposition and Entanglement',
                     'planck': 6.61e-2}], dict, {'message': 'I love Quantum Computing',
                                                 'message2': 'I love Superposition and Entanglement',
                                                 'planck': 6.61e-2}, 10, None
        if index == 12:
            return self._connectionParams['Client IP'], \
                   int(self._connectionParams['Client Port']), \
                   [Exception('Dummy exception')], str, "EXCEPTION FROM SENDER: " + str(Exception('Dummy exception')), \
                   10, 'NoAES'
        if index == 13:
            return self._connectionParams['Server IP'], \
                   int(self._connectionParams['Server Port']), \
                   [Exception('Dummy exception')], str, "EXCEPTION FROM RECEIVER: " + str(Exception('Dummy exception')), \
                   10, 'NoAES'

    def senderMethodMapper(self, index, transferProtocol):
        if index == 1:
            return transferProtocol.initiateConnection
        if index == 2:
            return transferProtocol.sendConfirmationInitiateConnection
        if index == 3:
            return transferProtocol.sendNegotiateParameters
        if index == 4:
            return transferProtocol.sendOT
        if index == 5:
            return transferProtocol.sendPRFKey
        if index == 6:
            return transferProtocol.sendPsiValues
        if index == 7:
            return transferProtocol.sendRSAReceiverPublicKey
        if index == 8:
            return transferProtocol.sendRSASenderPublicKey
        if index == 9:
            return transferProtocol.sendAESKeyByRSA
        if index == 10:
            return transferProtocol.sendIVByRSA
        if index == 11:
            return transferProtocol.sendBackNegotiateParameters
        if index == 12:
            return transferProtocol.sendErrorMessageFromSender
        if index == 13:
            return transferProtocol.sendErrorMessageFromReceiver

    def receiverMethodMapper(self, index, transferProtocol):
        if index == 1:
            return transferProtocol.receiveInitiateConnection
        if index == 2:
            return transferProtocol.receiveConfirmationInitiateConnection
        if index == 3:
            return transferProtocol.receiveNegotiateParameters
        if index == 4:
            return transferProtocol.receiveOT
        if index == 5:
            return transferProtocol.receiveKey
        if index == 6:
            return transferProtocol.receivePsiValues
        if index == 7:
            return transferProtocol.receiveRSAReceiverPublicKey
        if index == 8:
            return transferProtocol.receiveRSASenderPublicKey
        if index == 9:
            return transferProtocol.receiveAESKeyByRSA
        if index == 10:
            return transferProtocol.receiveIVByRSA
        if index == 11:
            return transferProtocol.receiveModifiedNegotiateParameters
        if index == 12:
            return transferProtocol.receiveErrorMessageFromSender
        if index == 13:
            return transferProtocol.receiveErrorMessageFromReceiver

    @parameterized.expand([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]])
    def test_sendMethods(self, index):
        # setup
        comSend = mock(ComSend)
        comReceive = mock(ComReceive)
        ip, port, data, datatype, toSend, headersize, flag = self.parametersMapper(index)

        # ----------------- when RSA exchange keys procedure -------------------------------
        if index in (7, 8):
            when(CryptoUtils).convertRSAKeyToString(data[0]).thenReturn(data[0])

        # ------------------ when AES key and iv exchange via RSA encryption ---------------------------

        if index in (9, 10):
            when(CryptoUtils).rsaEncrypt(data[0], data[1]).thenReturn(data[1])

        if flag is None:
            when(comSend).send(any(datatype), ip,
                               port,
                               HEADERSIZE=headersize)
        else:
            when(comSend).send(any(datatype), ip,
                               port,
                               HEADERSIZE=headersize, flag=flag)

        transferProtocol = TransferProtocol(self._connectionParams, comSend, comReceive)

        # execute
        if len(data) == 0:
            self.senderMethodMapper(index, transferProtocol)()
        elif len(data) == 1:
            self.senderMethodMapper(index, transferProtocol)(data[0])
        else:
            self.senderMethodMapper(index, transferProtocol)(data[1], data[0])

        # verify
        if index in (7, 8):
            verify(CryptoUtils).convertRSAKeyToString(data[0])
        if index in (9, 10):
            verify(CryptoUtils).rsaEncrypt(data[0], data[1])

        if flag == None:
            verify(comSend).send(toSend, ip, port, HEADERSIZE=headersize)
        else:
            verify(comSend).send(toSend, ip, port, HEADERSIZE=headersize, flag=flag)

        unstub()

    @parameterized.expand([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]])
    def test_sendMethodsFailWhenSendingExceptionOccurs(self, index):
        # setup
        comSend = mock(ComSend)
        comReceive = mock(ComReceive)
        ip, port, data, datatype, toSend, headersize, flag = self.parametersMapper(index)

        # ----------------- when RSA exchange keys procedure -------------------------------
        if index in (7, 8):
            when(CryptoUtils).convertRSAKeyToString(data[0]).thenReturn(data[0])

        # ------------------ when AES key and iv exchange via RSA encryption ---------------------------

        if index in (9, 10):
            when(CryptoUtils).rsaEncrypt(data[0], data[1]).thenReturn(data[1])

        exception = Exception('Bad Sending')
        if flag is None:
            when(comSend).send(any(datatype), ip,
                               port,
                               HEADERSIZE=headersize).thenRaise(exception)
        else:
            when(comSend).send(any(datatype), ip,
                               port,
                               HEADERSIZE=headersize, flag=flag).thenRaise(exception)

        transferProtocol = TransferProtocol(self._connectionParams, comSend, comReceive)

        # execute
        with self.assertRaises(Exception) as context:
            if len(data) == 0:
                self.senderMethodMapper(index, transferProtocol)()
            elif len(data) == 1:
                self.senderMethodMapper(index, transferProtocol)(data[0])
            else:
                self.senderMethodMapper(index, transferProtocol)(data[1], data[0])

            self.assertTrue('Bad Sending' in context.exception)

        # verify
        if index in (7, 8):
            verify(CryptoUtils).convertRSAKeyToString(data[0])
        if index in (9, 10):
            verify(CryptoUtils).rsaEncrypt(data[0], data[1])

        if flag == None:
            verify(comSend).send(toSend, ip, port, HEADERSIZE=headersize)
        else:
            verify(comSend).send(toSend, ip, port, HEADERSIZE=headersize, flag=flag)

        unstub()

    @parameterized.expand([[7], [8]])
    def test_sendMethodsFailWhenTransformingRSAKeyToStringExceptionOccurs(self, index):
        # setup
        comSend = mock(ComSend)
        comReceive = mock(ComReceive)
        ip, port, data, datatype, toSend, headersize, flag = self.parametersMapper(index)

        # ----------------- when RSA exchange keys procedure -------------------------------

        exception = Exception('Wrong convert RSA key to String')

        when(CryptoUtils).convertRSAKeyToString(data[0]).thenRaise(exception)

        transferProtocol = TransferProtocol(self._connectionParams, comSend, comReceive)

        # execute
        with self.assertRaises(Exception) as context:
            if len(data) == 0:
                self.senderMethodMapper(index, transferProtocol)()
            elif len(data) == 1:
                self.senderMethodMapper(index, transferProtocol)(data[0])
            else:
                self.senderMethodMapper(index, transferProtocol)(data[1], data[0])

            self.assertTrue('Wrong convert RSA key to String' in context.exception)

        # verify

        verify(CryptoUtils).convertRSAKeyToString(data[0])

        verify(comSend, times=0).send(toSend, ip, port, HEADERSIZE=headersize, flag=flag)

        unstub()

    @parameterized.expand([[9], [10]])
    def test_sendMethodsFailWhenEncryptingAESKeyOrIVWithPublicKeysFail(self, index):
        # setup
        comSend = mock(ComSend)
        comReceive = mock(ComReceive)
        ip, port, data, datatype, toSend, headersize, flag = self.parametersMapper(index)

        # ----------------- when RSA exchange keys procedure -------------------------------

        exception = Exception('Failing RSA encryption')

        when(CryptoUtils).rsaEncrypt(data[0], data[1]).thenRaise(exception)

        transferProtocol = TransferProtocol(self._connectionParams, comSend, comReceive)

        # execute
        with self.assertRaises(Exception) as context:
            if len(data) == 0:
                self.senderMethodMapper(index, transferProtocol)()
            elif len(data) == 1:
                self.senderMethodMapper(index, transferProtocol)(data[0])
            else:
                self.senderMethodMapper(index, transferProtocol)(data[1], data[0])

            self.assertTrue('Failing RSA encryption' in context.exception)

        # verify

        verify(CryptoUtils).rsaEncrypt(data[0], data[1])

        verify(comSend, times=0).send(toSend, ip, port, HEADERSIZE=headersize, flag=flag)

        unstub()

    # ----------------------------------------- RECEIVE METHODS -------------------------------------#

    @parameterized.expand([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]])
    def test_receiveMethods(self, index):
        # setup
        comSend = mock(ComSend)
        comReceive = mock(ComReceive)
        ip, port, data, datatype, toReceive, headersize, flag = self.parametersMapper(index)

        if flag is None:
            when(comReceive).receive(ip, port, HEADERSIZE=headersize).thenReturn(toReceive)
        else:
            when(comReceive).receive(ip, port, HEADERSIZE=headersize, flag=flag).thenReturn(toReceive)

        # ----------------- when RSA exchange keys procedure -------------------------------
        if index in (7, 8):
            when(CryptoUtils).stringToRSAKey(toReceive).thenReturn(toReceive)

        # ------------------ when AES key and iv exchange via RSA encryption ---------------------------

        if index in (9, 10):
            when(CryptoUtils).rsaDecrypt(data[0], toReceive).thenReturn(toReceive)

        transferProtocol = TransferProtocol(self._connectionParams, comSend, comReceive)

        # execute
        if len(data) != 2:
            response = self.receiverMethodMapper(index, transferProtocol)()
        else:
            response = self.receiverMethodMapper(index, transferProtocol)(data[0])

        # verify
        self.assertEqual(toReceive, response)
        if flag == None:
            verify(comReceive).receive(ip, port, HEADERSIZE=headersize)
        else:
            verify(comReceive).receive(ip, port, HEADERSIZE=headersize, flag=flag)

        if index in (7, 8):
            verify(CryptoUtils).stringToRSAKey(toReceive)
        if index in (9, 10):
            verify(CryptoUtils).rsaDecrypt(data[0], toReceive)

        unstub()

    @parameterized.expand([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]])
    def test_receiveMethodsFailsWhenReceivingExceptionOccurs(self, index):
        # setup
        comSend = mock(ComSend)
        comReceive = mock(ComReceive)
        ip, port, data, datatype, toReceive, headersize, flag = self.parametersMapper(index)

        exception = Exception('Bad Receiving')
        if flag is None:
            when(comReceive).receive(ip, port, HEADERSIZE=headersize).thenRaise(exception)
        else:
            when(comReceive).receive(ip, port, HEADERSIZE=headersize, flag=flag).thenRaise(exception)

        # ----------------- when RSA exchange keys procedure -------------------------------
        if index in (7, 8):
            when(CryptoUtils).stringToRSAKey(toReceive).thenReturn(toReceive)

        # ------------------ when AES key and iv exchange via RSA encryption ---------------------------

        if index in (9, 10):
            when(CryptoUtils).rsaDecrypt(data[0], toReceive).thenReturn(toReceive)

        transferProtocol = TransferProtocol(self._connectionParams, comSend, comReceive)

        # execute
        with self.assertRaises(Exception) as context:
            if len(data) != 2:
                self.receiverMethodMapper(index, transferProtocol)()
            else:
                self.receiverMethodMapper(index, transferProtocol)(data[0])
            self.assertTrue('Bad Receiving' in context.exception)

        # verify
        if flag == None:
            verify(comReceive).receive(ip, port, HEADERSIZE=headersize)
        else:
            verify(comReceive).receive(ip, port, HEADERSIZE=headersize, flag=flag)

        if index in (7, 8):
            verify(CryptoUtils, times=0).stringToRSAKey(toReceive)
        if index in (9, 10):
            verify(CryptoUtils, times=0).rsaDecrypt(data[0], toReceive)

        unstub()

    @parameterized.expand([[7], [8]])
    def test_receiveMethodsFailsWhenRSAConvertingStringToPEMFails(self, index):
        # setup
        comSend = mock(ComSend)
        comReceive = mock(ComReceive)
        ip, port, data, datatype, toReceive, headersize, flag = self.parametersMapper(index)

        exception = Exception('Wrong convert RSA String to key')
        if flag is None:
            when(comReceive).receive(ip, port, HEADERSIZE=headersize).thenReturn(toReceive)
        else:
            when(comReceive).receive(ip, port, HEADERSIZE=headersize, flag=flag).thenReturn(toReceive)

        # ----------------- when RSA exchange keys procedure -------------------------------

        when(CryptoUtils).stringToRSAKey(toReceive).thenRaise(exception)

        transferProtocol = TransferProtocol(self._connectionParams, comSend, comReceive)

        # execute
        with self.assertRaises(Exception) as context:
            if len(data) != 2:
                self.receiverMethodMapper(index, transferProtocol)()
            else:
                self.receiverMethodMapper(index, transferProtocol)(data[0])
            self.assertTrue('Wrong convert RSA String to key' in context.exception)

        # verify
        verify(comReceive).receive(ip, port, HEADERSIZE=headersize, flag=flag)

        verify(CryptoUtils).stringToRSAKey(toReceive)

        unstub()

    @parameterized.expand([[9], [10]])
    def test_receiveMethodsFailsWhenRSADecryptingAESKeyOrIVFails(self, index):
        # setup
        comSend = mock(ComSend)
        comReceive = mock(ComReceive)
        ip, port, data, datatype, toReceive, headersize, flag = self.parametersMapper(index)

        exception = Exception('Failing RSA decryption')
        if flag is None:
            when(comReceive).receive(ip, port, HEADERSIZE=headersize).thenReturn(toReceive)
        else:
            when(comReceive).receive(ip, port, HEADERSIZE=headersize, flag=flag).thenReturn(toReceive)

        # ----------------- when RSA exchange keys procedure -------------------------------

        when(CryptoUtils).rsaDecrypt(data[0], toReceive).thenRaise(exception)

        transferProtocol = TransferProtocol(self._connectionParams, comSend, comReceive)

        # execute
        with self.assertRaises(Exception) as context:
            if len(data) != 2:
                self.receiverMethodMapper(index, transferProtocol)()
            else:
                self.receiverMethodMapper(index, transferProtocol)(data[0])
            self.assertTrue('Failing RSA encryption' in context.exception)

        # verify
        verify(comReceive).receive(ip, port, HEADERSIZE=headersize, flag=flag)

        verify(CryptoUtils).rsaDecrypt(data[0], toReceive)

        unstub()
