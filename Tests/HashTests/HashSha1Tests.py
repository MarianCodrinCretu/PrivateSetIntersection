import _hashlib
import unittest
from Hash.HashSha1 import HashSha1


class HashSha1Tests(unittest.TestCase):
    def setUp(self):
        self._sha1HashUnderTest = HashSha1()

    def testGenerate_givenPlaintextAsBytesType_shouldReturnHash(self):
        # Arrange
        testPlaintext = b'test'
        expectedResult = b'\xa9J\x8f\xe5\xcc\xb1\x9b\xa6\x1cL\x08s\xd3\x91\xe9\x87\x98/\xbb\xd3'

        # Act
        actualResult = self._sha1HashUnderTest.generate(testPlaintext)

        # Assert
        self.assertEqual(expectedResult, actualResult)

    def testGenerate_givenPlaintextAsStringType_shouldThrowTypeException(self):
        # Arrange
        testPlaintext = 'test'

        # Act & Assert
        self.assertRaises(TypeError, self._sha1HashUnderTest.generate, testPlaintext)

    def testGenerate_givenEmptyByteTypeAsPlaintext_shouldReturnHash(self):
        # Arrange
        testPlaintext = b''
        expectedResult = b'\xda9\xa3\xee^kK\r2U\xbf\xef\x95`\x18\x90\xaf\xd8\x07\t'

        # Act
        actualResult = self._sha1HashUnderTest.generate(testPlaintext)

        # Assert
        self.assertEqual(expectedResult, actualResult)

    def testInitialize_shouldSetTheHashProperty(self):
        # Arrange
        # Act
        self._sha1HashUnderTest.initialize()

        # Assert
        self.assertIsInstance(self._sha1HashUnderTest._hash, _hashlib.HASH)
