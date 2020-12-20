import _hashlib
import unittest
from Hash.HashMd5 import HashMd5


class HashMd5Tests(unittest.TestCase):
    def setUp(self):
        self._expectedOutputByteLength = 16
        self._md5HashUnderTest = HashMd5(self._expectedOutputByteLength)

    def testGenerate_givenPlaintextAsBytesType_shouldReturnHashOfBytesType(self):
        # Arrange
        testPlaintext = b'test'
        expectedResult = b"\t\x8fk\xcdF!\xd3s\xca\xdeN\x83&'\xb4\xf6"

        # Act
        actualResult = self._md5HashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenPlaintextAsStringType_shouldReturnHashOfBytesType(self):
        # Arrange
        testPlaintext = 'test'

        # Act
        actualResult = self._md5HashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertIsInstance(actualResult, bytes)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenEmptyByteTypeAsPlaintext_shouldReturnHashOfBytesType(self):
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
