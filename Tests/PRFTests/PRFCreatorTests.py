import unittest

from aspectlib import Aspect, Return, weave
from PRF.AESPrfCreator import AESPrfCreator
from PRF.AESPrf import AESPrf
from PRF.DESPrfCreator import DESPrfCreator
from PRF.DESPrf import DESPrf


class PRFCreatorTests(unittest.TestCase):

    def testComputePrf_givenAESInstanceAsPrfAndPlaintextAsBytesOfBlockSizeLength_shouldReturnComputedPrf(self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testIv, testKey)
        testAESPrfCreatorInstance = AESPrfCreator(testIv, testKey)

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            testPlaintext = b'This is a key123'
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputePrf_givenDESInstanceAsPrfAndPlaintextAsBytesOfBlockSizeLength_shouldReturnComputedPrf(self):
        testIv = b'testtest'
        testKey = b'testtest'
        testAESPrfInstance = DESPrf(testIv, testKey)
        testAESPrfCreatorInstance = DESPrfCreator(testIv, testKey)
        testPlaintext = b'This is a key123'

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputePrf_givenAESInstanceAsPrfAndPlaintextAsStringOfBlockSizeLength_shouldThrowTypeError(self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testIv, testKey)
        testAESPrfCreatorInstance = AESPrfCreator(testIv, testKey)
        testPlaintext = 'This is an IV456'

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputePrf_givenDESInstanceAsPrfAndPlaintextAsStringOfBlockSizeLength_shouldReturnComputedPrf(self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = DESPrfCreator(testIv, testKey)
        testPlaintext = 'This is an IV456'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputePrf_givenAESInstanceAsPrfAndPlaintextAsBytesOfDifferentBlockSize_shouldThrowTypeError(self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testIv, testKey)
        testAESPrfCreatorInstance = AESPrfCreator(testIv, testKey)
        testPlaintext = b'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputePrf_givenDESInstanceAsPrfAndPlaintextAsBytesOfDifferentBlockSize_shouldReturnComputedPrf(self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = DESPrfCreator(testIv, testKey)
        testPlaintext = b'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputePrf_givenAESInstanceAsPrfAndPlaintextAsStringOfDifferentBlockSize_shouldThrowTypeError(self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testIv, testKey)
        testAESPrfCreatorInstance = AESPrfCreator(testIv, testKey)
        testPlaintext = 'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputePrf_givenDESInstanceAsPrfAndPlaintextAsStringOfDifferentBlockSize_shouldReturnComputedPrf(self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = DESPrfCreator(testIv, testKey)
        testPlaintext = 'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)