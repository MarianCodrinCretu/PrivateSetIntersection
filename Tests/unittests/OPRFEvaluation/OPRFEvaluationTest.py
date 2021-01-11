from unittest import TestCase
from unittest.mock import create_autospec, patch, Mock

from mockito import when, mock, unstub, verify
from parameterized import parameterized

from CommunicationService.TransferProtocol import TransferProtocol
from OPRFEvaluation.OPRFEvaluation import OPRFEvaluation


def dummyHash1(x):
    pass


def dummyHash2(x):
    pass


def dummyPRF(x, key, l1, w, m, prf):
    pass


class OPRFEvaluationTest(TestCase):

    @parameterized.expand([['dummyKey'], [[1, 2]]])
    def test_sendKeyOrPsiValues(self, parameter):

        # setup
        transferProtocol = mock(TransferProtocol)
        if parameter == 'dummyKey':
            when(transferProtocol).sendPRFKey(parameter)
        else:
            when(transferProtocol).sendPsiValues(parameter)

        # execute
        oprfEvaluation = OPRFEvaluation(transferProtocol)
        if parameter == 'dummyKey':
            oprfEvaluation.sendKeyToSender(parameter)
        else:
            oprfEvaluation.sendSenderPsiValuesToReceiver(parameter)

        # verify
        if parameter == 'dummyKey':
            verify(transferProtocol).sendPRFKey(parameter)
        else:
            verify(transferProtocol).sendPsiValues(parameter)

        unstub()

    @parameterized.expand([['dummyKey'], [[1, 2]]])
    def test_sendKeyOrPsiValuesFails(self, parameter):

        # setup
        key = 'dummyKey'
        transferProtocol = mock(TransferProtocol)
        exception = Exception('Fails send')
        if parameter == 'dummyKey':
            when(transferProtocol).sendPRFKey(parameter).thenRaise(exception)
        else:
            when(transferProtocol).sendPsiValues(parameter).thenRaise(exception)

        # execute
        with self.assertRaises(Exception) as context:
            oprfEvaluation = OPRFEvaluation(transferProtocol)
            if parameter == 'dummyKey':
                oprfEvaluation.sendKeyToSender(parameter)
            else:
                oprfEvaluation.sendSenderPsiValuesToReceiver(parameter)
            self.assertEqual(str(exception), context.exception)

        # verify
        if parameter == 'dummyKey':
            verify(transferProtocol).sendPRFKey(parameter)
        else:
            verify(transferProtocol).sendPsiValues(parameter)

        unstub()

    @parameterized.expand([['dummyKey'], [[1, 2]]])
    def test_receiveKeyOrPsiValues(self, parameter):
        # setup
        transferProtocol = mock(TransferProtocol)
        if parameter == 'dummyKey':
            when(transferProtocol).receiveKey().thenReturn(parameter)
        else:
            when(transferProtocol).receivePsiValues().thenReturn(parameter)

        oprfEvaluation = OPRFEvaluation(transferProtocol)
        if parameter == 'dummyKey':
            result = oprfEvaluation.receiveKeyFromReceiver()
        else:
            result = oprfEvaluation.receiveSenderPsiValues()
        self.assertEqual(result, parameter)

        # verify
        if parameter == 'dummyKey':
            verify(transferProtocol).receiveKey()
        else:
            verify(transferProtocol).receivePsiValues()

        unstub()

    @parameterized.expand([['dummyKey'], [[1, 2]]])
    def test_receiveKeyOrPsiValuesFails(self, parameter):

        # setup
        transferProtocol = mock(TransferProtocol)
        exception = Exception('Fails receive')
        if parameter == 'dummyKey':
            when(transferProtocol).receiveKey().thenRaise(parameter)
        else:
            when(transferProtocol).receivePsiValues().thenRaise(exception)

        # execute
        with self.assertRaises(Exception) as context:
            oprfEvaluation = OPRFEvaluation(transferProtocol)
            if parameter == 'dummyKey':
                oprfEvaluation.receiveKeyFromReceiver()
            else:
                oprfEvaluation.receiveSenderPsiValues()
            self.assertEqual(str(exception), context.exception)

        # verify
        if parameter == 'dummyKey':
            verify(transferProtocol).receiveKey()
        else:
            verify(transferProtocol).receivePsiValues()

        unstub()

    def test_generatePsiValues(self):

        # setup
        dictParameters = {
            'w': 2,
            'l1': 128,
            'm': 100,
            'prf': 'AES'
        }
        data = ['data']
        mockFunctionHash1 = create_autospec(dummyHash1, return_value='hash1')
        mockFunctionHash2 = create_autospec(dummyHash2, return_value='hash2')
        mockFunctionPRF = create_autospec(dummyPRF, return_value=[1, 1])
        transferProtocol = mock(TransferProtocol)

        # execute
        oprfEvaluation = OPRFEvaluation(transferProtocol)
        result = oprfEvaluation.generateSenderPsiValues("key", [[1, 1], [0, 0]], data, dictParameters,
                                                        mockFunctionHash1, mockFunctionHash2, mockFunctionPRF)

        # verify
        self.assertEqual(result, ['hash2'])

        unstub()
    @parameterized.expand([[1],[2],[3]])
    def test_generatePsiValuesFailsDueToDifferentException(self, index):

        # setup
        dictParameters = {
            'w': 2,
            'l1': 128,
            'm': 100,
            'prf': 'AES'
        }
        data = ['data']
        exceptionHash1 = Exception('Hash 1 computing exception')
        exceptionHash2 = Exception('Hash 2 computing exception')
        exceptionPRF = Exception('PRF computing exception')


        mockFunctionHash1 = Mock(return_value = 'exceptionHash1')
        if index == 1:
            mockFunctionHash1.side_effect = exceptionHash1

        mockFunctionHash2 = Mock(side_effect = exceptionHash2, return_value = 'exceptionHash2')
        if index == 2:
            mockFunctionHash2.side_effect = exceptionHash2

        mockFunctionPRF = Mock(side_effect = exceptionPRF, return_value='exceptionPRF')
        if index == 3:
            mockFunctionPRF.side_effect = exceptionPRF

        transferProtocol = mock(TransferProtocol)

        # execute
        oprfEvaluation = OPRFEvaluation(transferProtocol)
        with self.assertRaises(Exception) as context:
            oprfEvaluation.generateSenderPsiValues("key", [[1, 1], [0, 0]], data, dictParameters,
                                                            mockFunctionHash1, mockFunctionHash2, mockFunctionPRF)
            if index==1:
                self.assertEqual(str(exceptionHash1), context.exception)
            if index==2:
                self.assertEqual(str(exceptionHash2), context.exception)
            if index==3:
                self.assertEqual(str(exceptionPRF), context.exception)

        unstub()

    def test_evaluatePsiValues(self):

        # setup
        dictParameters = {
            'w': 2,
            'l1': 128,
            'm': 100,
            'prf': 'AES'
        }
        data = ['data', 'data2']
        mockFunctionHash1 = create_autospec(dummyHash1, return_value='hash1')
        mockFunctionHash2 = create_autospec(dummyHash2, return_value='hash2')
        mockFunctionPRF = create_autospec(dummyPRF, return_value=[1, 1])
        transferProtocol = mock(TransferProtocol)

        # execute
        oprfEvaluation = OPRFEvaluation(transferProtocol)
        result = oprfEvaluation.evaluatePsiValues("key", ['hash2', 'hash2'], [[1, 1], [0, 0]], data, dictParameters,
                                                  mockFunctionHash1, mockFunctionHash2, mockFunctionPRF)

        # verify
        self.assertEqual(result, ['data', 'data2'])

        unstub()

    @parameterized.expand([[1], [2], [3]])
    def test_evaluatePsiValuesFailsDueToDifferentException(self, index):

        # setup
        dictParameters = {
            'w': 2,
            'l1': 128,
            'm': 100,
            'prf': 'AES'
        }
        data = ['data']
        exceptionHash1 = Exception('Hash 1 computing exception')
        exceptionHash2 = Exception('Hash 2 computing exception')
        exceptionPRF = Exception('PRF computing exception')

        mockFunctionHash1 = Mock(return_value='exceptionHash1')
        if index == 1:
            mockFunctionHash1.side_effect = exceptionHash1

        mockFunctionHash2 = Mock(side_effect=exceptionHash2, return_value='exceptionHash2')
        if index == 2:
            mockFunctionHash2.side_effect = exceptionHash2

        mockFunctionPRF = Mock(side_effect=exceptionPRF, return_value='exceptionPRF')
        if index == 3:
            mockFunctionPRF.side_effect = exceptionPRF

        transferProtocol = mock(TransferProtocol)

        # execute
        oprfEvaluation = OPRFEvaluation(transferProtocol)
        with self.assertRaises(Exception) as context:
            oprfEvaluation.evaluatePsiValues("key", ['hash2', 'hash2'], [[1, 1], [0, 0]], data, dictParameters,
                                                   mockFunctionHash1, mockFunctionHash2, mockFunctionPRF)
            if index == 1:
                self.assertEqual(str(exceptionHash1), context.exception)
            if index == 2:
                self.assertEqual(str(exceptionHash2), context.exception)
            if index == 3:
                self.assertEqual(str(exceptionPRF), context.exception)

        unstub()
