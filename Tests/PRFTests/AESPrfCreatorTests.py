import unittest
from PRF.AESPrfCreator import AESPrfCreator
from PRF.AESPrf import AESPrf


class AESPrfCreatorTests(unittest.TestCase):
    def setUp(self):
        testKey = 'This is a key123'.encode("utf8")
        testIV = 'This is an IV456'.encode("utf8")
        self._AESPrfCreatorUnderTest = AESPrfCreator(testIV, testKey)

    def testCreatePrf_shouldReturnAESPrfInstance(self):
        # Arrange
        # Act
        actualResult = self._AESPrfCreatorUnderTest.createPrf()

        # Assert
        self.assertIsInstance(actualResult, AESPrf)


if __name__ == '__main__':
    unittest.main()
