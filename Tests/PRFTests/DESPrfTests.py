# import unittest
#
# from PRF.PRFCreator import PRFCreator
# from Shared.Enums.PrfTypeEnum import PrfTypeEnum
#
#
# class DESPrfTests(unittest.TestCase):
#
#     def setUp(self):
#         testKey = b'-8B key-'
#         testIV = 'This is '.encode("utf8")
#         self._DESPrfUnderTest = PRFCreator(PrfTypeEnum.DES, testKey, testIV)
#
#     def testComputePrf_givenPlaintextOfSameLengthAsKeyAndIVAsUTF8_shouldReturnComputedPRFAsByteType(self):
#         # Arrange
#         testPlaintext = 'testtext'.encode("utf8")
#         expected = b'J\xb8\x03\x93f\xba\xa1\xf2'
#
#         # Act
#         actual = self._DESPrfUnderTest.computePrf(testPlaintext)
#
#         # Assert
#         self.assertEqual(expected, actual)
#
#     def testComputePrf_givenPlaintextOfDifferentLengthAsKeyAndIVAsUTF8_shouldThrowValueError(self):
#         # Arrange
#         testPlaintext = 'Random text of different length'.encode("utf8")
#
#         # Act
#         actual = self._DESPrfUnderTest.computePrf(testPlaintext)
#
#         # Assert
#         self.assertEqual(expected, actual)
#
#     def testComputePrf_givenPlaintextOfSameLengthAsKeyAndIVNotAsUTF8_shouldThrowTypeException(self):
#         # Arrange
#         testPlaintext = 'testtext'
#
#         # Act & Assert
#         self.assertRaises(TypeError, self._DESPrfUnderTest.computePrf, testPlaintext)
#
#     def testComputePrf_givenEmptyPlaintextAsUTF8_shouldReturnEmptyAsByteType(self):
#         # Arrange
#         testPlaintext = ''.encode("utf8")
#         expected = b''
#
#         # Act
#         actual = self._DESPrfUnderTest.computePrf(testPlaintext)
#
#         # Assert
#         self.assertEqual(expected, actual)
#
#
# if __name__ == '__main__':
#     unittest.main()
