import unittest

from Crypto.Cipher import DES3

from PRF.DES3Prf import DES3Prf
from Shared.Enums.PrfScopeEnum import PrfScopeEnum


class DES33PrfTests(unittest.TestCase):

    def setUp(self):
        self._testKey = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        self._testIV = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        self._DES3PrfUnderTest = DES3Prf(self._testKey, self._testIV)

    def testComputePrf_givenPlaintextOfBlockSizeAsUTF8AndNoScope_shouldReturnComputedPRFAsByteTypeConsideringGenericScope(
            self):
        # Arrange
        testPlaintext = b'E\x8b\x88\xcb\xd1\xadW\x957Oq[\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        # Act
        actual = self._DES3PrfUnderTest.computePrf(testPlaintext)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockSizeAsUTF8AndGenericScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = b'E\x8b\x88\xcb\xd1\xadW\x957Oq[\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        # Act
        actual = self._DES3PrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERIC)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsUTF8AndPRGScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = b'E\x8b\x88\xcb\xd1\xadW\x957Oq[\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        # Act
        actual = self._DES3PrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.PRG)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsUTF8AndGeneratorScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = b'E\x8b\x88\xcb\xd1\xadW\x957Oq[\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        # Act
        actual = self._DES3PrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERATOR)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsStringAndNoScope_shouldReturnComputedPRFAsByteTypeConsideringGenericScope(
            self):
        # Arrange
        testPlaintext = 'E\x8b\x88\xcb\xd1\xadW\x957Oq[\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        # Act
        actual = self._DES3PrfUnderTest.computePrf(testPlaintext)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsStringAndGenericScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'E\x8b\x88\xcb\xd1\xadW\x957Oq[\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        # Act
        actual = self._DES3PrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERIC)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsStringAndPRGScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'E\x8b\x88\xcb\xd1\xadW\x957Oq[\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        # Act
        actual = self._DES3PrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.PRG)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsStringAndGeneratorScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = b'E\x8b\x88\xcb\xd1\xadW\x957Oq[\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        # Act
        actual = self._DES3PrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERATOR)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfDifferentBlockLengthAsStringAndGenericScope_shouldReturnComputedPRFAsByteType(
            self):
        # Arrange
        testPlaintext = 'E\x8b\x88\xcb\xd1\xadW\13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        # Act
        actual = self._DES3PrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERIC)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfDifferentBlockLengthAsStringAndPRGScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = b'E\x8b\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        # Act
        actual = self._DES3PrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.PRG)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfDifferentBlockLengthAsStringAndGeneratorScope_shouldRaiseValueError(self):
        # Arrange
        testPlaintext = b'E\x8b\xa9s\xa7\x82'
        # Act & Assert
        self.assertRaises(ValueError, self._DES3PrfUnderTest.computePrf, testPlaintext, PrfScopeEnum.GENERATOR)

    def testComputePrf_givenPlaintextOfDifferentBlockLengthAsByteAndGeneratorScope_shouldRaiseValueError(self):
        # Arrange
        testPlaintext = 'This'

        # Act & Assert
        self.assertRaises(ValueError, self._DES3PrfUnderTest.computePrf, testPlaintext, PrfScopeEnum.GENERATOR)

    def testGetAlgorithm_shouldReturnDES3(self):
        # Arrange
        expected = DES3

        # Act
        actual = self._DES3PrfUnderTest.getAlgorithm()

        # Assert
        self.assertEqual(expected, actual)

    def testGetEncryptionAlgorithms_shouldReturnMoDES3ScopeDictionary(self):
        # Arrange
        # Act
        actual = self._DES3PrfUnderTest.getEncryptionAlgorithms()

        # Assert
        self.assertIsNotNone(actual)


if __name__ == '__main__':
    unittest.main()
