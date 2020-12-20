import _hashlib
import unittest
from Hash.HashSha512 import HashSha512


class HashSha512Tests(unittest.TestCase):
    def setUp(self):
        self._expectedOutputByteLength = 64
        self._sha512HashUnderTest = HashSha512(self._expectedOutputByteLength)

    def testGenerate_givenPlaintextAsBytesType_shouldReturnHash(self):
        # Arrange
        testPlaintext = b'test'
        expectedResult = b'\xee&\xb0\xddJ\xf7\xe7I\xaa\x1a\x8e\xe3\xc1\n\xe9\x92?a\x89\x80w.G?\x88\x19\xa5\xd4\x94\x0e\r\xb2z\xc1\x85\xf8\xa0\xe1\xd5\xf8O\x88\xbc\x88\x7f\xd6{\x1472\xc3\x04\xcc_\xa9\xad\x8eoW\xf5\x00(\xa8\xff'

        # Act
        actualResult = self._sha512HashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenPlaintextAsStringType_shouldReturnHash(self):
        # Arrange
        testPlaintext = 'test'

        # Act
        actualResult = self._sha512HashUnderTest.generate(testPlaintext)
        actualResultByteLength = len(actualResult)

        # Assert
        self.assertIsInstance(actualResult, bytes)
        self.assertEqual(self._expectedOutputByteLength, actualResultByteLength)

    def testGenerate_givenEmptyByteTypeAsPlaintext_shouldReturnHash(self):
        # Arrange
        testPlaintext = b''
        expectedResult = b"\xcf\x83\xe15~\xef\xb8\xbd\xf1T(P\xd6m\x80\x07\xd6 \xe4\x05\x0bW\x15\xdc\x83\xf4\xa9!\xd3l\xe9\xceG\xd0\xd1<]\x85\xf2\xb0\xff\x83\x18\xd2\x87~\xec/c\xb91\xbdGAz\x81\xa582z\xf9'\xda>"


        # Act
        actualResult = self._sha512HashUnderTest.generate(testPlaintext)

        # Assert
        self.assertEqual(expectedResult, actualResult)

    def testInitialize_shouldSetTheHashProperty(self):
        # Arrange
        # Act
        self._sha512HashUnderTest.initialize()

        # Assert
        self.assertIsInstance(self._sha512HashUnderTest._hash, _hashlib.HASH)
