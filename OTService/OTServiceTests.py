import unittest
from mockito import when, mock, verify, unstub, expect
import OTService


class OTServiceTests(unittest.TestCase):

    def test_sender_OT(self):
        # Arrange
        transferProtocol = mock()
        ot = OTService.OTService(transferProtocol)
        matrix_A = [[0, 1, 0], [0, 1, 0], [1, 1, 0]]
        matrix_B = [[0, 1, 0], [0, 0, 1], [0, 1, 1]]
        data_sent = [{"A": [0, 0, 1], "B": [0, 0, 0]}, {"A": [1, 1, 1], "B": [1, 0, 1]}, {"A": [0, 0, 0], "B": [0, 1, 1]}]
        m = 3
        w = 3
        s = "000"
        expected_result = [[0, 1, 0], [0, 1, 0], [1, 1, 0]]

        # Act
        when(transferProtocol).receiveOT().thenReturn(data_sent[0], data_sent[1], data_sent[2])
        actual_result = ot.senderOT(s, w, m)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_sender_random_OT(self):
        # Arrange
        transferProtocol = mock()
        ot = OTService.OTService(transferProtocol)
        matrix_A = [[0, 1, 0], [0, 1, 0], [1, 1, 0]]
        matrix_B = [[0, 1, 0], [0, 0, 1], [0, 1, 1]]
        r_i1 = [1, 0, 1]
        data_sent = [{"r_0": [0, 0, 1], "r_1": r_i1, "delta": [1, 0, 1]},
                     {"r_0": [1, 1, 1], "r_1": r_i1, "delta": [0, 0, 0]},
                     {"r_0": [0, 0, 0], "r_1": r_i1, "delta": [1, 1, 0]}]
        m = 3
        w = 3
        s = "010"
        expected_result = [[0, 1, 0], [0, 0, 0], [1, 1, 0]]

        # Act
        when(transferProtocol).receiveOT().thenReturn(data_sent[0], data_sent[1], data_sent[2])
        actual_result = ot.sender_randomOT(s, w, m)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_receiver_OT(self):
        # Arrange
        transferProtocol = mock()
        ot = OTService.OTService(transferProtocol)
        matrix_A = [[0, 1, 0], [0, 1, 0], [1, 1, 0]]
        matrix_B = [[0, 1, 0], [0, 0, 1], [0, 1, 1]]
        m = 3
        w = 3

        # Act
        when(transferProtocol).sendOT()
        ot.receiverOT(matrix_A, matrix_B, w, m)

        # Assert
        verify(transferProtocol).sendOT({'A': [0, 0, 1], 'B': [0, 0, 0]})
        verify(transferProtocol).sendOT({"A": [1, 1, 1], "B": [1, 0, 1]})
        verify(transferProtocol).sendOT({"A": [0, 0, 0], "B": [0, 1, 1]})

        unstub()

    def test_receiver__random_OT(self):
        # Arrange
        transferProtocol = mock()
        ot = OTService.OTService(transferProtocol)
        matrix_A = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1]]
        matrix_B = [[1, 1, 0], [0, 1, 1], [0, 1, 1], [1, 0, 0]]
        m = 4
        w = 3

        # Act
        when(transferProtocol).sendOT()
        ot.receiverOT(matrix_A, matrix_B, w, m)

        # Assert
        verify(transferProtocol).sendOT({'A': [0, 0, 0, 0], 'B': [1, 0, 0, 1]})
        verify(transferProtocol).sendOT({"A": [1, 1, 1, 0], "B": [1, 1, 1, 0]})
        verify(transferProtocol).sendOT({"A": [0, 0, 0, 1], "B": [0, 1, 1, 0]})

        unstub()


if __name__ == "__main__":
    unittest.main()
