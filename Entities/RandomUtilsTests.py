import unittest
from Utils.Utils import RandomUtils, PSIAlgoUtils


class TestRandomUtils(unittest.TestCase):
    def test_generateSSender_length_equal_w(self):
        s = RandomUtils.generateSSender(5)
        self.assertEqual(len(s), 5, "s should have 5 elements")

    def test_generateSSender_just_bits(self):
        s = RandomUtils.generateSSender(5)
        for b in s:
            self.assertIn(b, ['0', '1'], "s should contain only 1 and 0")

    def test_initMatrixDReceiver_length(self):
        D = RandomUtils.initMatrixDReceiver(3, 5)
        self.assertEqual(len(D), 3, "D should have 3 columns")
        self.assertEqual(len(D[0]), 5, "D should have 5 lines")
        self.assertEqual(len(D[1]), 5, "D should have 5 lines")
        self.assertEqual(len(D[2]), 5, "D should have 5 lines")

    def test_initMatrixDReceiver_contains_just_1(self):
        D = RandomUtils.initMatrixDReceiver(3, 5)
        for l in range(len(D)):
            for c in range(len(D[l])):
                self.assertEqual(D[l][c], 1, "D should contain only 1's at initialization")

    def test_initMatrixAReceiver_length(self):
        A = RandomUtils.initMatrixAReceiver(3, 5)
        self.assertEqual(len(A), 3, "A should have 3 columns")
        self.assertEqual(len(A[0]), 5, "A should have 5 lines")
        self.assertEqual(len(A[1]), 5, "A should have 5 lines")
        self.assertEqual(len(A[2]), 5, "A should have 5 lines")

    def test_initMatrixAReceiver_just_bits(self):
        A = RandomUtils.initMatrixAReceiver(3, 5)
        for l in range(len(A)):
            for c in range(len(A[l])):
                self.assertIn(A[l][c], [0, 1], "A should contain only 0 or 1")

    def test_generateKey_length_equal_w(self):
        key = RandomUtils.generateKey(5)
        self.assertEqual(len(key), 5, "the key should have length 5")

    def test_generateKey_just_bits(self):
        key = RandomUtils.generateKey(5)
        for b in key:
            self.assertIn(b, ["0", "1"], "the key should contain only 1 and 0")


if __name__ == "__main__":
    unittest.main()
