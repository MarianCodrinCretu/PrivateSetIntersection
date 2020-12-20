import unittest

from Crypto.Cipher import AES

from PRF.AESPrf import AESPrf
from Shared.Enums.PrfScopeEnum import PrfScopeEnum


class AESPrfTests(unittest.TestCase):
    def setUp(self) -> None:
        self._testKey = 'This is a key123'.encode("utf8")
        self._testIV = 'This is an IV456'.encode("utf8")
        self._AESPrfUnderTest = AESPrf(self._testKey, self._testIV)

    def testComputePrf_givenPlaintextOfBlockSizeAsUTF8AndNoScope_shouldReturnComputedPRFAsByteTypeConsideringGenericScope(
            self):
        # Arrange
        testPlaintext = 'This is an IV456'.encode("utf8")

        # Act
        actual = self._AESPrfUnderTest.computePrf(testPlaintext)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockSizeAsUTF8AndGenericScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is an IV456'.encode("utf8")

        # Act
        actual = self._AESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERIC)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsUTF8AndPRGScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is an IV456'.encode("utf8")

        # Act
        actual = self._AESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.PRG)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsUTF8AndGeneratorScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is an IV456'.encode("utf8")

        # Act
        actual = self._AESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERATOR)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsStringAndNoScope_shouldReturnComputedPRFAsByteTypeConsideringGenericScope(
            self):
        # Arrange
        testPlaintext = 'This is an IV456'

        # Act
        actual = self._AESPrfUnderTest.computePrf(testPlaintext)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsStringAndGenericScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is an IV456'

        # Act
        actual = self._AESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERIC)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsStringAndPRGScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is an IV456'

        # Act
        actual = self._AESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.PRG)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsStringAndGeneratorScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is an IV456'

        # Act
        actual = self._AESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERATOR)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfDifferentBlockLengthAsStringAndGenericScope_shouldReturnComputedPRFAsByteType(
            self):
        # Arrange
        testPlaintext = 'This is an '

        # Act
        actual = self._AESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERIC)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfDifferentBlockLengthAsStringAndPRGScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is'

        # Act
        actual = self._AESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.PRG)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfDifferentBlockLengthAsStringAndGeneratorScope_shouldRaiseValueError(self):
        # Arrange
        testPlaintext = 'This is '

        # Act & Assert
        self.assertRaises(ValueError, self._AESPrfUnderTest.computePrf, testPlaintext, PrfScopeEnum.GENERATOR)

    def testComputePrf_givenPlaintextOfDifferentBlockLengthAsByteAndGeneratorScope_shouldRaiseValueError(self):
        # Arrange
        testPlaintext = 'This is '

        # Act & Assert
        self.assertRaises(ValueError, self._AESPrfUnderTest.computePrf, testPlaintext, PrfScopeEnum.GENERATOR)

    def testGetAlgorithm_shouldReturnAES(self):
        # Arrange
        expected = AES

        # Act
        actual = self._AESPrfUnderTest.getAlgorithm()

        #Assert
        self.assertEqual(expected, actual)

    def testGetEncryptionAlgorithms_shouldReturnModesScopeDictionary(self):
        #Arrange
        #Act
        actual = self._AESPrfUnderTest.getEncryptionAlgorithms()

        #Assert
        self.assertIsNotNone(actual)


if __name__ == '__main__':
    unittest.main()
