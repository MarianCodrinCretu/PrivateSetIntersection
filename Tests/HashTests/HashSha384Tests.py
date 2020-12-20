import _hashlib
import unittest
from Hash.HashSha384 import HashSha384


class HashSha384Tests(unittest.TestCase):
    def setUp(self):
        self._expectedOutputByteLength = 48
        self._sha384HashUnderTest = HashSha384(self._expectedOutputByteLength)

    def testGenerate_givenPlaintextAsBytesType_shouldReturnHash(self):
        # Arrange
        testPlaintext = b'test'

        # Act
        actualResult = self._sha384HashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertIsInstance(actualResult, bytes)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenPlaintextAsStringType_shouldReturnHashOfBytesType(self):
        # Arrange
        testPlaintext = 'test'

        # Act
        actualResult = self._sha384HashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertIsInstance(actualResult, bytes)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenEmptyByteTypeAsPlaintext_shouldReturnHash(self):
        # Arrange
        testPlaintext = b''

        # Act
        actualResult = self._sha384HashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertIsInstance(actualResult, bytes)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testInitialize_shouldSetTheHashProperty(self):
        # Arrange
        # Act
        self._sha384HashUnderTest.initialize()

        # Assert
        self.assertIsInstance(self._sha384HashUnderTest._hash, _hashlib.HASH)
