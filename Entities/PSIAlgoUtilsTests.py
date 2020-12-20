import unittest
from Utils.Utils import RandomUtils, PSIAlgoUtils


class TestPSIAlgoUtils(unittest.TestCase):
    def test_computeBReceiver_same_number_of_lines(self):
        with self.assertRaises(Exception) as context:
            B = PSIAlgoUtils.computeBReceiver([[0]], [[0], [1]])

        self.assertTrue('A and D should have same number of lines' in str(context.exception))

    def test_computeBReceiver_same_number_of_columns(self):
        with self.assertRaises(Exception) as context:
            B = PSIAlgoUtils.computeBReceiver([[0], [0, 1]], [[0], [1]])

        self.assertTrue('A and D should have same number of columns' in str(context.exception))

    def test_computeBReceiver_00(self):
        B = PSIAlgoUtils.computeBReceiver([[0, 0], [0, 0]], [[0, 0], [0, 0]])
        self.assertEqual(B, [[0, 0], [0, 0]], "0 xor 0 = 0")

    def test_computeBReceiver_11(self):
        B = PSIAlgoUtils.computeBReceiver([[1, 1], [1, 1]], [[1, 1], [1, 1]])
        self.assertEqual(B, [[0, 0], [0, 0]], "1 xor 1 = 0")

    def test_computeBReceiver_10(self):
        B = PSIAlgoUtils.computeBReceiver([[0, 0], [0, 0]], [[1, 1], [1, 1]])
        self.assertEqual(B, [[1, 1], [1, 1]], "1 xor 0 = 0 xor 1 = 1")


if __name__ == "__main__":
    unittest.main()
