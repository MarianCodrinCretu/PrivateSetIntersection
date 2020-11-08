import _blake2
import unittest
from Hash.HashBlake2b import HashBlake2b


class HashBlake2bTests(unittest.TestCase):
    def setUp(self):
        self._blake2bHashUnderTest = HashBlake2b()

    def testGenerate_givenPlaintextAsBytesType_shouldReturnHashOfBytesType(self):
        # Arrange
        testPlaintext = b'test'

        # Act
        actualResult = self._blake2bHashUnderTest.generate(testPlaintext)

        # Assert
        self.assertIsInstance(actualResult, bytes)

    def testGenerate_givenPlaintextAsStringType_shouldThrowTypeException(self):
        # Arrange
        testPlaintext = 'test'

        # Act & Assert
        self.assertRaises(TypeError, self._blake2bHashUnderTest.generate, testPlaintext)

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
