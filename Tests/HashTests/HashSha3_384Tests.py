import hashlib
import unittest

from Hash.Sha3_384 import HashSha3_384


class HashSha3_384Tests(unittest.TestCase):
    def setUp(self):
        self._expectedOutputByteLength = 48
        self._sha3_384HashUnderTest = HashSha3_384(self._expectedOutputByteLength)

    def testGenerate_givenPlaintextAsBytesType_shouldReturnHash(self):
        # Arrange
        testPlaintext = b'test'
        expectedResult = b"\xe5\x16\xda\xbb#\xb6\xe3\x00&\x865C('\x80\xa3\xae\r\xcc\xf0UQ\xcf\x02\x95\x17\x8d\x7f\xf0\xf1\xb4\x1e\xec\xb9\xdb?\xf2\x19\x00|N\tr`\xd5\x86!\xbd"

        # Act
        actualResult = self._sha3_384HashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenPlaintextAsStringType_shouldReturnHashOfBytesType(self):
        # Arrange
        testPlaintext = 'test'

        # Act
        actualResult = self._sha3_384HashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertIsInstance(actualResult, bytes)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenEmptyByteTypeAsPlaintext_shouldReturnHash(self):
        # Arrange
        testPlaintext = b''
        expectedResult = b'\x0cc\xa7[\x84^O}\x01\x10}\x85.L$\x85\xc5\x1aP\xaa\xaa\x94\xfca\x99^q\xbb\xee\x98:*\xc3q81&J\xdbG\xfbk\xd1\xe0X\xd5\xf0\x04'

        # Act
        actualResult = self._sha3_384HashUnderTest.generate(testPlaintext)

        # Assert
        self.assertEqual(expectedResult, actualResult)

    def testInitialize_shouldSetTheHashProperty(self):
        # Arrange
        # Act
        self._sha3_384HashUnderTest.initialize()

        # Assert
        self.assertIsInstance(self._sha3_384HashUnderTest._hash, hashlib.sha3_384)
