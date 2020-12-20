import unittest
from PRF.OPRF import computeOPrfValue
from Shared.Enums.PrfTypeEnum import PrfTypeEnum


class OPRFTests(unittest.TestCase):

    def testComputeOPrfValue_givenCorrectParametersForAESUsingAES_shouldReturnCorrectV(self):
        # Arrange
        testL1 = 256
        testKey = b'0101010101011111'
        testPlaintext = b'00000000000000000000000000000000'
        testW = 633
        testM = 16777216

        # Act
        actualV = computeOPrfValue(testPlaintext, testKey, testL1, testW, testM, PrfTypeEnum.AES)
        actualVLength = len(actualV)

        # Assert
        self.assertEqual(actualVLength, testW)

    def testComputeOPrfValue_givenCorrectParametersForDESUsingDES_shouldReturnCorrectV(self):
        # Arrange
        testL1 = 128
        testKey = b'01010101'
        testPlaintext = b'0000000000000000'
        testW = 633
        testM = 16777216

        # Act
        actualV = computeOPrfValue(testPlaintext, testKey, testL1, testW, testM, PrfTypeEnum.DES)
        actualVLength = len(actualV)

        # Assert
        self.assertEqual(actualVLength, testW)

    def testComputeOPrfValue_givenCorrectParametersForDES3UsingDES3_shouldReturnCorrectV(self):
        # Arrange
        testL1 = 384
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testPlaintext = b'000000000000000000000000000000000000000000000001'
        testW = 633
        testM = 16777216

        # Act
        actualV = computeOPrfValue(testPlaintext, testKey, testL1, testW, testM, PrfTypeEnum.DES3)
        actualVLength = len(actualV)

        # Assert
        self.assertEqual(actualVLength, testW)

    def testComputeOPrfValue_givenCorrectParametersForAESUsingAESAndPlaintextOfStringType_shouldReturnCorrectV(self):
        # Arrange
        testL1 = 256
        testKey = b'0101010101011111'
        testPlaintext = '00000000000000000000000000000000'
        testW = 633
        testM = 16777216

        # Act
        actualV = computeOPrfValue(testPlaintext, testKey, testL1, testW, testM, PrfTypeEnum.AES)
        actualVLength = len(actualV)

        # Assert
        self.assertEqual(actualVLength, testW)

    def testComputeOPrfValue_givenCorrectParametersForDESUsingDESAndPlaintextOfStringType_shouldReturnCorrectV(self):
        # Arrange
        testL1 = 128
        testKey = b'01010101'
        testPlaintext = '0000000000000000'
        testW = 633
        testM = 16777216

        # Act
        actualV = computeOPrfValue(testPlaintext, testKey, testL1, testW, testM, PrfTypeEnum.DES)
        actualVLength = len(actualV)

        # Assert
        self.assertEqual(actualVLength, testW)

    def testComputeOPrfValue_givenCorrectParametersForDES3UsingDES3AndPlaintextOfStringType_shouldReturnCorrectV(self):
        # Arrange
        testL1 = 384
        testKey = b'E\xfa\xa1\xe7\xaf\xc1\x1b.B\x11\x07#v\xfcE\x8b\xf1\x11\x9a\xbd\xb9f\xd9\xbf'
        testPlaintext = '000000000000000000000000000000000000000000000001'
        testW = 633
        testM = 16777216

        # Act
        actualV = computeOPrfValue(testPlaintext, testKey, testL1, testW, testM, PrfTypeEnum.DES3)
        actualVLength = len(actualV)

        # Assert
        self.assertEqual(actualVLength, testW)

    def testComputeOPrfValue_givenIncorrectParametersForAESUsingAES_shouldRaiseException(self):
        # Arrange
        testL1 = 256
        testKey = b'0101010101011111'
        testPlaintext = b'00000000000000000000000000000000'
        testW = 0
        testM = 16777216

        # Act & Assert
        self.assertRaises(Exception, computeOPrfValue, testPlaintext, testKey, testL1, testW, testM, PrfTypeEnum.AES)

    def testComputeOPrfValue_givenIncorrectParametersForDESUsingDES_shouldRaiseException(self):
        # Arrange
        testL1 = 0
        testKey = b'01010101'
        testPlaintext = b'0000000000000000'
        testW = 633
        testM = 16777216

        # Act & Assert
        self.assertRaises(Exception, computeOPrfValue, testPlaintext, testKey, testL1, testW, testM, PrfTypeEnum.DES)

    def testComputeOPrfValue_givenIncorrectParametersForDES3UsingDES3_shouldRaiseException(self):
        # Arrange
        testL1 = 384
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testPlaintext = b'000000000000000000000000000000000000000000000001'
        testW = 633
        testM = 0

        # Act & Assert
        self.assertRaises(Exception, computeOPrfValue, testPlaintext, testKey, testL1, testW, testM, PrfTypeEnum.DES3)


if __name__ == '__main__':
    unittest.main()
