import unittest

from aspectlib import Aspect, Return, weave
from PRF.AESPrf import AESPrf
from PRF.DES3Prf import DES3Prf
from PRF.DESPrf import DESPrf
from PRF.PRFCreator import PRFCreator
from Shared.Enums.PrfScopeEnum import PrfScopeEnum
from Shared.Enums.PrfTypeEnum import PrfTypeEnum


class PRFCreatorTests(unittest.TestCase):

    def testComputeAESPrf_givenPlaintextAsBytesOfBlockSizeLengthAndNoScopeSpecified_shouldComputePrfConsideringGenericScopeSet(
            self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testKey, testIv)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            testPlaintext = b'This is a key123'
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDESPrf_givenPlaintextAsBytesOfBlockSizeLengthAndNoScopeSpecified_shouldComputePrfConsideringGenericScopeSet(
            self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = b'This is a key123'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDES3Prf_givenPlaintextAsBytesOfBlockSizeLengthAndNoScopeSpecified_shouldComputePrfConsideringGenericScopeSet(
            self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = b'E\x8b\x88\xcb\xd1\xadW\x957Oq[\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDES3PrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputeAESPrf_givenPlaintextAsBytesOfBlockSizeLengthAndPRGScope_shouldReturnComputedPrf(self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testKey, testIv)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            testPlaintext = b'This is a key123'
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDESPrf_givenPlaintextAsBytesOfBlockSizeLengthAndPRGScope_shouldReturnComputedPrf(self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = b'This is a key123'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDES3Prf_givenPlaintextAsBytesOfBlockSizeLengthAndPRGScope_shouldReturnComputedPrf(self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = b'E\x8b\x88\xcb\xd1\xadW\x957Oq[\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDES3PrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeAESPrf_givenPlaintextAsBytesOfBlockSizeLengthAndGeneratorScope_shouldReturnComputedPrf(self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testKey, testIv)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            testPlaintext = b'This is a key123'
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDESPrf_givenPlaintextAsBytesOfBlockSizeLengthAndGeneratorScope_shouldReturnComputedPrf(self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = b'This is a key123'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.GENERATOR)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDES3Prf_givenPlaintextAsBytesOfBlockSizeLengthAndGeneratorScope_shouldReturnComputedPrf(self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = b'E\x8b\x88\xcb\xd1\xadW\x957Oq[\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDES3PrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.GENERATOR)
            self.assertIsInstance(actualResult, bytes)

    def testComputeAESPrf_givenPlaintextAsBytesOfDifferentBlockSizeAndNoScopeSpecified_shouldComputePrfConsideringGenericScope(
            self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testIv, testKey)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)
        testPlaintext = b'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDESPrf_givenPlaintextAsBytesOfDifferentBlockSizeAndNoScopeSpecified_shouldComputePrfConsideringGenericScope(
            self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = b'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDES3Prf_givenPlaintextAsBytesOfDifferentBlockSizeAndNoScopeSpecified_shouldComputePrfConsideringGenericScope(
            self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = b'E\x8b\x88\xcb\xd1\xadW\x957Oq['

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDES3PrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputeAESPrf_givenPlaintextAsBytesOfDifferentBlockSizeAndPRGScope_shouldComputePrf(self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testIv, testKey)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)
        testPlaintext = b'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDESPrf_givenPlaintextAsBytesOfDifferentBlockSizeAndPRGScope_shouldComputePrf(self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = b'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDES3Prf_givenPlaintextAsBytesOfDifferentBlockSizeAndPRGScope_shouldComputePrf(
            self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = b'E\x8b\x88\xcb\xd1\xadW\x957Oq['

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDES3PrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeAESPrf_givenPlaintextAsBytesOfDifferentBlockSizeAndGeneratorScope_shouldRaiseValueError(
            self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testIv, testKey)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)
        testPlaintext = b'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            self.assertRaises(ValueError, testAESPrfCreatorInstance.computePrf, testPlaintext, PrfScopeEnum.GENERATOR)

    def testComputeDESPrf_givenPlaintextAsBytesOfDifferentBlockSizeAndGeneratorScope_shouldRaiseValueError(
            self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = b'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            self.assertRaises(ValueError, testDESPrfCreatorInstance.computePrf, testPlaintext, PrfScopeEnum.GENERATOR)

    def testComputeDES3Prf_givenPlaintextAsBytesOfDifferentBlockSizeAndGeneratorScope_shouldRaiseValueError(
            self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = b'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            self.assertRaises(ValueError, testDES3PrfCreatorInstance.computePrf, testPlaintext, PrfScopeEnum.GENERATOR)

    def testComputeAESPrf_givenPlaintextAsBytesOfDifferentBlockSizeAndGenericScope_shouldComputePrf(
            self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testIv, testKey)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)
        testPlaintext = b'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.GENERIC)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDESPrf_givenPlaintextAsBytesOfDifferentBlockSizeAndGenericScope_shouldComputePrf(
            self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = b'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.GENERIC)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDES3Prf_givenPlaintextAsBytesOfDifferentBlockSizeAndGenericScope_shouldComputePrf(
            self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = b'E\x8b\x88\xcb\xd1\xadW\x957Oq['

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDES3PrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.GENERIC)
            self.assertIsInstance(actualResult, bytes)

    def testComputeAESPrf_givenPlaintextAsStringOfBlockSizeLengthAndNoScopeSpecified_shouldComputePrfConsideringGenericScopeSet(
            self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testKey, testIv)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            testPlaintext = 'This is a key123'
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDESPrf_givenPlaintextAsStringOfBlockSizeLengthAndNoScopeSpecified_shouldComputePrfConsideringGenericScopeSet(
            self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = 'This is a key123'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDES3Prf_givenPlaintextAsStringOfBlockSizeLengthAndNoScopeSpecified_shouldComputePrfConsideringGenericScopeSet(
            self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = 'E\x8b\x88\xcb\xd1\xadW\x957Oq[\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDES3PrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputeAESPrf_givenPlaintextAsStringOfBlockSizeLengthAndPRGScope_shouldReturnComputedPrf(self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testKey, testIv)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            testPlaintext = 'This is a key123'
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDESPrf_givenPlaintextAsStringOfBlockSizeLengthAndPRGScope_shouldReturnComputedPrf(self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = 'This is a key123'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDES3Prf_givenPlaintextAsStringOfBlockSizeLengthAndPRGScope_shouldReturnComputedPrf(self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = 'E\x8b\x88\xcb\xd1\xadW\x957Oq[\xa0\xdd#\x13\x06\xed\xaf\xa6\xa9s\xa7\x82'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDES3PrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeAESPrf_givenPlaintextAsStringOfBlockSizeLengthAndGeneratorScope_shouldReturnComputedPrf(self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testKey, testIv)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            testPlaintext = 'This is a key123'
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDESPrf_givenPlaintextAsStringOfBlockSizeLengthAndGeneratorScope_shouldReturnComputedPrf(self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = 'This is a key123'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.GENERATOR)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDES3Prf_givenPlaintextAsStringOfBlockSizeLengthAndGeneratorScope_shouldReturnComputedPrf(self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = 'We are no longer the knights who say ni!'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDES3PrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.GENERATOR)
            self.assertIsInstance(actualResult, bytes)

    def testComputeAESPrf_givenPlaintextAsStringOfDifferentBlockSizeAndNoScopeSpecified_shouldComputePrfConsideringGenericScope(
            self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testIv, testKey)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)
        testPlaintext = 'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDESPrf_givenPlaintextAsStringOfDifferentBlockSizeAndNoScopeSpecified_shouldComputePrfConsideringGenericScope(
            self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = 'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDES3Prf_givenPlaintextAsStringOfDifferentBlockSizeAndNoScopeSpecified_shouldComputePrfConsideringGenericScope(
            self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = 'E\x8b\x88\xcb\xd1\xadW\x957Oq['

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDES3PrfCreatorInstance.computePrf(testPlaintext)
            self.assertIsInstance(actualResult, bytes)

    def testComputeAESPrf_givenPlaintextAsStringOfDifferentBlockSizeAndPRGScope_shouldComputePrf(self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testIv, testKey)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)
        testPlaintext = 'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDESPrf_givenPlaintextAsStringOfDifferentBlockSizeAndPRGScope_shouldComputePrf(self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = 'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDES3Prf_givenPlaintextAsStringOfDifferentBlockSizeAndPRGScope_shouldComputePrf(
            self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = 'E\x8b\x88\xcb\xd1\xadW\x957Oq['

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDES3PrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.PRG)
            self.assertIsInstance(actualResult, bytes)

    def testComputeAESPrf_givenPlaintextAsStringOfDifferentBlockSizeAndGeneratorScope_shouldRaiseValueError(
            self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testIv, testKey)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)
        testPlaintext = 'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            self.assertRaises(ValueError, testAESPrfCreatorInstance.computePrf, testPlaintext, PrfScopeEnum.GENERATOR)

    def testComputeDESPrf_givenPlaintextAsStringOfDifferentBlockSizeAndGeneratorScope_shouldRaiseValueError(
            self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = 'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            self.assertRaises(ValueError, testDESPrfCreatorInstance.computePrf, testPlaintext, PrfScopeEnum.GENERATOR)

    def testComputeDES3Prf_givenPlaintextAsStringOfDifferentBlockSizeAndGeneratorScope_shouldRaiseValueError(
            self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = 'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            self.assertRaises(ValueError, testDES3PrfCreatorInstance.computePrf, testPlaintext, PrfScopeEnum.GENERATOR)

    def testComputeAESPrf_givenPlaintextAsStringOfDifferentBlockSizeAndGenericScope_shouldComputePrf(
            self):
        testIv = b'This is a key123'
        testKey = b'This is an IV456'
        testAESPrfInstance = AESPrf(testIv, testKey)
        testAESPrfCreatorInstance = PRFCreator(PrfTypeEnum.AES, testKey, testIv)
        testPlaintext = 'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testAESPrfInstance)

        with weave(testAESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testAESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.GENERIC)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDESPrf_givenPlaintextAsStringOfDifferentBlockSizeAndGenericScope_shouldComputePrf(
            self):
        testIv = b'testtest'
        testKey = b'testtest'
        testDESPrfInstance = DESPrf(testIv, testKey)
        testDESPrfCreatorInstance = PRFCreator(PrfTypeEnum.DES, testKey, testIv)
        testPlaintext = 'test'

        @Aspect
        def mock_getPrf(self):
            yield Return(testDESPrfInstance)

        with weave(testDESPrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDESPrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.GENERIC)
            self.assertIsInstance(actualResult, bytes)

    def testComputeDES3Prf_givenPlaintextAsStringOfDifferentBlockSizeAndGenericScope_shouldComputePrf(
            self):
        testIv = b'\xdf\x8b\xf6[\xfb\xaf\t"\xa14wM\xda\xfd\x0c\xd0g\x1c\x10D>\xd9\x86\x8b'
        testKey = b'R@\xd6\x91\x7f)\xb1XE\x02\x91\xe4\xd0\x84;\x0b\xbd\x12\xb5\xa9j\x12.\x8e'
        testDES3PrfInstance = DES3Prf(testIv, testKey)
        testDES3PrfCreatorInstance = PRFCreator(PrfTypeEnum.DES3, testKey, testIv)
        testPlaintext = 'E\x8b\x88\xcb\xd1\xadW\x957Oq['

        @Aspect
        def mock_getPrf(self):
            yield Return(testDES3PrfInstance)

        with weave(testDES3PrfCreatorInstance.getPrf, mock_getPrf):
            actualResult = testDES3PrfCreatorInstance.computePrf(testPlaintext, PrfScopeEnum.GENERIC)
            self.assertIsInstance(actualResult, bytes)


