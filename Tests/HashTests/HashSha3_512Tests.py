import hashlib
import unittest
from Hash.Sha3_512 import HashSha3_512


class HashSha3_512Tests(unittest.TestCase):
    def setUp(self):
        self._expectedOutputByteLength = 64
        self._sha3_512HashUnderTest = HashSha3_512(self._expectedOutputByteLength)

    def testGenerate_givenPlaintextAsBytesType_shouldReturnHash(self):
        # Arrange
        testPlaintext = b'test'
        expectedResult = b'\x9e\xce\x08n\x9b\xacI\x1f\xac\\\x1d\x10F\xca\x11\xd77\xb9*+.\xbd\x93\xf0\x05\xd7\xb7\x10\x11\x0c\ng\x82\x88\x16n\x7f\xbeyh\x83\xa4\xf2\xe9\xb3\xca\x9fHOR\x1d\x0c\xe4d4\\\xc1\xae\xc9gy\x14\x9c\x14'

        # Act
        actualResult = self._sha3_512HashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenPlaintextAsStringType_shouldReturnHashOfBytesType(self):
        # Arrange
        testPlaintext = 'test'

        # Act
        actualResult = self._sha3_512HashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertIsInstance(actualResult, bytes)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenEmptyByteTypeAsPlaintext_shouldReturnHash(self):
        # Arrange
        testPlaintext = b''
        expectedResult = b'\xa6\x9fs\xcc\xa2:\x9a\xc5\xc8\xb5g\xdc\x18Zun\x97\xc9\x82\x16O\xe2XY\xe0\xd1\xdc\xc1G\\\x80\xa6\x15\xb2\x12:\xf1\xf5\xf9L\x11\xe3\xe9@,:\xc5X\xf5\x00\x19\x9d\x95\xb6\xd3\xe3\x01u\x85\x86(\x1d\xcd&'

        # Act
        actualResult = self._sha3_512HashUnderTest.generate(testPlaintext)

        # Assert
        self.assertEqual(expectedResult, actualResult)

    def testInitialize_shouldSetTheHashProperty(self):
        # Arrange
        # Act
        self._sha3_512HashUnderTest.initialize()

        # Assert
        self.assertIsInstance(self._sha3_512HashUnderTest._hash, hashlib.sha3_512)
