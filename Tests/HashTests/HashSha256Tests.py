import _hashlib
import unittest
from Hash.HashSha256 import HashSha256


class HashSha256Tests(unittest.TestCase):
    def setUp(self):
        self._sha256HashUnderTest = HashSha256()

    def testGenerate_givenPlaintextAsBytesType_shouldReturnHash(self):
        # Arrange
        testPlaintext = b'test'
        expectedResult = b'\x9f\x86\xd0\x81\x88L}e\x9a/\xea\xa0\xc5Z\xd0\x15\xa3\xbfO\x1b+\x0b\x82,\xd1]l\x15\xb0\xf0\n\x08'

        # Act
        actualResult = self._sha256HashUnderTest.generate(testPlaintext)

        # Assert
        self.assertEqual(expectedResult, actualResult)

    def testGenerate_givenPlaintextAsStringType_shouldThrowTypeException(self):
        # Arrange
        testPlaintext = 'test'

        # Act & Assert
        self.assertRaises(TypeError, self._sha256HashUnderTest.generate, testPlaintext)

    def testGenerate_givenEmptyByteTypeAsPlaintext_shouldReturnHash(self):
        # Arrange
        testPlaintext = b''
        expectedResult = b"\xe3\xb0\xc4B\x98\xfc\x1c\x14\x9a\xfb\xf4\xc8\x99o\xb9$'\xaeA\xe4d\x9b\x93L\xa4\x95\x99\x1bxR\xb8U"

        # Act
        actualResult = self._sha256HashUnderTest.generate(testPlaintext)

        # Assert
        self.assertEqual(expectedResult, actualResult)

    def testInitialize_shouldSetTheHashProperty(self):
        # Arrange
        # Act
        self._sha256HashUnderTest.initialize()

        # Assert
        self.assertIsInstance(self._sha256HashUnderTest._hash, _hashlib.HASH)
