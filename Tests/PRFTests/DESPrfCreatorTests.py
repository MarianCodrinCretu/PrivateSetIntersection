import unittest
from PRF.DESPrfCreator import DESPrfCreator
from PRF.DESPrf import DESPrf


class DESPrfCreatorTests(unittest.TestCase):
    def setUp(self):
        testKey = b'-8B key-'
        testIV = 'This is '.encode("utf8")
        self._DESPrfCreatorUnderTest = DESPrfCreator(testIV, testKey)

    def testCreatePrf_shouldReturnDESPrfInstance(self):
        # Arrange
        # Act
        actualResult = self._DESPrfCreatorUnderTest.createPrf()

        # Assert
        self.assertIsInstance(actualResult, DESPrf)


if __name__ == '__main__':
    unittest.main()
