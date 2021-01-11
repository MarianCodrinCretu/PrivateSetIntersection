import unittest
import Precomputation
from mockito import when


class TestPrecomputation(unittest.TestCase):

    def test_compute_v(self):
        # Arrange
        precomputation = Precomputation.Precomputation("Dummy")
        expected_output = [0, 0, 0]

        # Act
        when(precomputation).computePRF("1", "2", "3").thenReturn([0, 0, 0])
        when(precomputation).computeHash1("1", "3").thenReturn("1")
        actual_output = precomputation.compute_v("1", "2", "3")

        # Assert
        self.assertEqual(expected_output, actual_output)

    def test_compute_v_list(self):
        # Arrange
        precomputation = Precomputation.Precomputation("Dummy")
        input_list = ["1", "1", "1", "1"]
        expected_output = 4

        # Act
        when(precomputation).computePRF("1", "2", "3").thenReturn([0, 0, 0])
        when(precomputation).computeHash1("1", "3").thenReturn("1")
        actual_output = precomputation.compute_v_list(input_list, "2", "3")

        # Assert
        self.assertEqual(expected_output, len(actual_output))

    def test_update_d(self):
        # Arrange
        v_list = [[1, 0, 2], [0, 2, 1], [1, 2, 0]]
        matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected_output = [[0, 0, 1], [0, 1, 0], [0, 0, 0]]
        precomputation = Precomputation.Precomputation("Dummy")

        # Act
        actual_output = precomputation.update_d(v_list, matrix)

        # Assert
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
