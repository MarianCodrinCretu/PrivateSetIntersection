# import unittest
#
#
# class AESPrfTests(unittest.TestCase):
#
#     def setUp(self):
#         testKey = 'This is a key123'.encode("utf8")
#         testIV = 'This is an IV456'.encode("utf8")
#         self._AESPrfUnderTest = AESPrfCreator(testIV, testKey)
#
#     def testComputePrf_givenPlaintextOfSameLengthAsKeyAndIVAsUTF8_shouldReturnComputedPRFAsByteType(self):
#         # Arrange
#         testPlaintext = 'This is an IV456'.encode("utf8")
#         expected = b'Kn\xaa\xb7\xbfI\xbf\\\x8a\xec\x8bX\xa4\x9a5\xe3'
#
#         # Act
#         actual = self._AESPrfUnderTest.computePrf(testPlaintext)
#
#         # Assert
#         self.assertEqual(expected, actual)
#
#     def testComputePrf_givenPlaintextOfDifferentLengthAsKeyAndIVAsUTF8_shouldThrowValueError(self):
#         # Arrange
#         testPlaintext = 'Random text of different length'.encode("utf8")
#
#         # Act & Assert
#         self.assertRaises(ValueError, self._AESPrfUnderTest.computePrf, testPlaintext)
#
#     def testComputePrf_givenPlaintextOfSameLengthAsKeyAndIVNotAsUTF8_shouldThrowTypeException(self):
#         # Arrange
#         testPlaintext = 'This is an IV456'
#
#         # Act & Assert
#         self.assertRaises(TypeError, self._AESPrfUnderTest.computePrf, testPlaintext)
#
#     def testComputePrf_givenEmptyPlaintextAsUTF8_shouldReturnEmptyAsByteType(self):
#         # Arrange
#         testPlaintext = ''.encode("utf8")
#         expected = b''
#
#
#         # Act
#         actual = self._AESPrfUnderTest.computePrf(testPlaintext)
#
#         # Assert
#         self.assertEqual(expected, actual)
#
#
# if __name__ == '__main__':
#     unittest.main()
