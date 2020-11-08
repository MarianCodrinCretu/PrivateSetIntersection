import _hashlib
import unittest
from Hash.HashMd5 import HashMd5


class HashMd5Tests(unittest.TestCase):
    def setUp(self):
        self._md5HashUnderTest = HashMd5()

    def testGenerate_givenPlaintextAsBytesType_shouldReturnHash(self):
        # Arrange
        testPlaintext = b'test'
        expectedResult = b"\t\x8fk\xcdF!\xd3s\xca\xdeN\x83&'\xb4\xf6"

        # Act
        actualResult = self._md5HashUnderTest.generate(testPlaintext)

        # Assert
        self.assertEqual(expectedResult, actualResult)

    def testGenerate_givenPlaintextAsStringType_shouldThrowTypeException(self):
        # Arrange
        testPlaintext = 'test'

        # Act & Assert
        self.assertRaises(TypeError, self._md5HashUnderTest.generate, testPlaintext)

    def testGenerate_givenEmptyByteTypeAsPlaintext_shouldReturnHash(self):
        # Arrange
        testPlaintext = b''
        expectedResult = b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~'

        # Act
        actualResult = self._md5HashUnderTest.generate(testPlaintext)

        # Assert
        self.assertEqual(expectedResult, actualResult)

    def testInitialize_shouldSetTheHashProperty(self):
        # Arrange
        # Act
        self._md5HashUnderTest.initialize()

        # Assert
        self.assertIsInstance(self._md5HashUnderTest._hash, _hashlib.HASH)


if __name__ == '__main__':
    unittest.main()
