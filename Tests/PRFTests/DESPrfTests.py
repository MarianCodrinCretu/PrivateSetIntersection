import unittest

from Crypto.Cipher import DES

from PRF.DESPrf import DESPrf
from Shared.Enums.PrfScopeEnum import PrfScopeEnum


class DESPrfTests(unittest.TestCase):

    def setUp(self):
        self._testKey = b'-8B key-'
        self._testIV = 'This is '.encode("utf8")
        self._DESPrfUnderTest = DESPrf(self._testKey, self._testIV)

    def testComputePrf_givenPlaintextOfBlockSizeAsUTF8AndNoScope_shouldReturnComputedPRFAsByteTypeConsideringGenericScope(
            self):
        # Arrange
        testPlaintext = b'testtext'

        # Act
        actual = self._DESPrfUnderTest.computePrf(testPlaintext)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockSizeAsUTF8AndGenericScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is an IV456'.encode("utf8")

        # Act
        actual = self._DESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERIC)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsUTF8AndPRGScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is an IV456'.encode("utf8")

        # Act
        actual = self._DESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.PRG)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsUTF8AndGeneratorScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is an IV456'.encode("utf8")

        # Act
        actual = self._DESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERATOR)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsStringAndNoScope_shouldReturnComputedPRFAsByteTypeConsideringGenericScope(
            self):
        # Arrange
        testPlaintext = 'This is an IV456'

        # Act
        actual = self._DESPrfUnderTest.computePrf(testPlaintext)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsStringAndGenericScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is an IV456'

        # Act
        actual = self._DESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERIC)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsStringAndPRGScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is an IV456'

        # Act
        actual = self._DESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.PRG)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfBlockLengthAsStringAndGeneratorScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is an IV456'

        # Act
        actual = self._DESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERATOR)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfDifferentBlockLengthAsStringAndGenericScope_shouldReturnComputedPRFAsByteType(
            self):
        # Arrange
        testPlaintext = 'This is an '

        # Act
        actual = self._DESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.GENERIC)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfDifferentBlockLengthAsStringAndPRGScope_shouldReturnComputedPRFAsByteType(self):
        # Arrange
        testPlaintext = 'This is'

        # Act
        actual = self._DESPrfUnderTest.computePrf(testPlaintext, PrfScopeEnum.PRG)

        # Assert
        self.assertIsInstance(actual, bytes)

    def testComputePrf_givenPlaintextOfDifferentBlockLengthAsStringAndGeneratorScope_shouldRaiseValueError(self):
        # Arrange
        testPlaintext = 'This'

        # Act & Assert
        self.assertRaises(ValueError, self._DESPrfUnderTest.computePrf, testPlaintext, PrfScopeEnum.GENERATOR)

    def testComputePrf_givenPlaintextOfDifferentBlockLengthAsByteAndGeneratorScope_shouldRaiseValueError(self):
        # Arrange
        testPlaintext = 'This'

        # Act & Assert
        self.assertRaises(ValueError, self._DESPrfUnderTest.computePrf, testPlaintext, PrfScopeEnum.GENERATOR)

    def testGetAlgorithm_shouldReturnDES(self):
        # Arrange
        expected = DES

        # Act
        actual = self._DESPrfUnderTest.getAlgorithm()

        # Assert
        self.assertEqual(expected, actual)

    def testGetEncryptionAlgorithms_shouldReturnModesScopeDictionary(self):
        # Arrange
        # Act
        actual = self._DESPrfUnderTest.getEncryptionAlgorithms()

        # Assert
        self.assertIsNotNone(actual)

if __name__ == '__main__':
    unittest.main()

