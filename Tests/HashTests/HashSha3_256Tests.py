import hashlib
import unittest
from Hash.HashSha3_256 import HashSha3_256


class HashSha3_256Tests(unittest.TestCase):
    def setUp(self):
        self._expectedOutputByteLength = 32
        self._sha3_256HashUnderTest = HashSha3_256(self._expectedOutputByteLength)

    def testGenerate_givenPlaintextAsBytesType_shouldReturnHash(self):
        # Arrange
        testPlaintext = b'test'
        expectedResult = b"6\xf0(X\x0b\xb0,\xc8'*\x9a\x02\x0fB\x00\xe3F\xe2v\xaefNE\xee\x80tUt\xe2\xf5\xab\x80"

        # Act
        actualResult = self._sha3_256HashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenPlaintextAsStringType_shouldReturnHashOfBytesType(self):
        # Arrange
        testPlaintext = 'test'

        # Act
        actualResult = self._sha3_256HashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertIsInstance(actualResult, bytes)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenEmptyByteTypeAsPlaintext_shouldReturnHash(self):
        # Arrange
        testPlaintext = b''
        expectedResult = b'\xa7\xff\xc6\xf8\xbf\x1e\xd7fQ\xc1GV\xa0a\xd6b\xf5\x80\xffM\xe4;I\xfa\x82\xd8\nK\x80\xf8CJ'

        # Act
        actualResult = self._sha3_256HashUnderTest.generate(testPlaintext)

        # Assert
        self.assertEqual(expectedResult, actualResult)

    def testInitialize_shouldSetTheHashProperty(self):
        # Arrange
        # Act
        self._sha3_256HashUnderTest.initialize()

        # Assert
        print()
        self.assertIsInstance(self._sha3_256HashUnderTest._hash, hashlib.sha3_256)
