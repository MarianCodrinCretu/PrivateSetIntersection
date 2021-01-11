import _blake2
import unittest
from Hash.HashBlake2b import HashBlake2b


class HashBlake2bTests(unittest.TestCase):
    def setUp(self):
        self._expectedOutputByteLength = 64
        self._blake2bHashUnderTest = HashBlake2b(self._expectedOutputByteLength)


    def testGenerate_givenPlaintextAsBytesType_shouldReturnHashOfBytesType(self):
        # Arrange
        testPlaintext = b'test'

        # Act
        actualResult = self._blake2bHashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertIsInstance(actualResult, bytes)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenPlaintextAsStringType_shouldReturnHashOfBytesType(self):
        testPlaintext = 'test'

        # Act
        actualResult = self._blake2bHashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertIsInstance(actualResult, bytes)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenEmptyByteTypeAsPlaintext_shouldReturnHashOfBytesType(self):
        # Arrange
        testPlaintext = b''

        # Act
        actualResult = self._blake2bHashUnderTest.generate(testPlaintext)

        # Assert
        self.assertIsInstance(actualResult, bytes)

    def testInitialize_shouldSetTheHashProperty(self):
        # Arrange
        # Act
        self._blake2bHashUnderTest.initialize()

        # Assert
        self.assertIsInstance(self._blake2bHashUnderTest._hash, _blake2.blake2b)
