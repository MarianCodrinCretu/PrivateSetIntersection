from unittest import TestCase

from NegotiationParameters.NegotiateParametersUtils import NegotiateParametersUtils
import NegotiationParameters.Constants

dictParameters = {
    'lambda': 128,
    'sigma': 60,
    'm': 0.75,
    'w': 100,
    'l1': 256,
    'l2': 50,
    'hash1': 'MD5',
    'hash2': 'SHA256',
    'prf': 'AES',
    'otVariant': '1',
    'lenDataset': 1000000
}

class NegotiateParametersUtilsTest(TestCase):


    negotiateParametersUtils = NegotiateParametersUtils()

    def test_ifValidTypeOfHash1ThenTypeNotModified(self):
        #setup
        copyDict = dictParameters.copy()
        #execute
        resultedDict=self.negotiateParametersUtils.validateParameters(copyDict)
        #verify
        self.assertEqual(copyDict['hash1'], resultedDict['hash1'])

    def test_ifNotValidTypeOfHash1ThenTypeModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['hash1']='MyHash'
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        self.assertEqual(NegotiationParameters.Constants.DEFAULT_HASH, resultedDict['hash1'])

    def test_ifValidTypeOfHash2ThenTypeNotModified(self):
        # setup
        copyDict = dictParameters.copy()
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        self.assertEqual(copyDict['hash2'], resultedDict['hash2'])

    def test_ifNotValidTypeOfHash2ThenTypeModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['hash2'] = 'MyHash'
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.DEFAULT_HASH, resultedDict['hash2'])

    def test_ifValidTypeOfPRFThenTypeNotModified(self):
        # setup
        copyDict = dictParameters.copy()
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        self.assertEqual(copyDict['prf'], resultedDict['prf'])

    def test_ifNotValidTypeOfPRFThenTypeModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['prf'] = 'MyPRF'
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.DEFAULT_PRF, resultedDict['prf'])

    def test_ifValidTypeOfOtVariantThenTypeNotModified(self):
        # setup
        copyDict = dictParameters.copy()
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        self.assertEqual(int(copyDict['otVariant']), resultedDict['otVariant'])

    def test_ifNotValidTypeOfOtVariantThenTypeModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['otVariant'] = '3'
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.DEFAULT_OT, int(resultedDict['otVariant']))

    def test_ifValidLambdaThenNotModified(self):
        # setup
        copyDict = dictParameters.copy()
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        self.assertEqual(copyDict['lambda'], resultedDict['lambda'])

    def test_ifLowerLambdaThenModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['lambda'] = 127
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.LAMBDA, resultedDict['lambda'])

    def test_ifNotValidLambdaThenModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['lambda'] = 'MyLambda'
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.LAMBDA, resultedDict['lambda'])

    def test_ifValidSigmaThenNotModified(self):
        # setup
        copyDict = dictParameters.copy()
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        self.assertEqual(copyDict['sigma'], resultedDict['sigma'])

    def test_ifLowerSigmaThenModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['sigma'] = 25
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.SIGMA, resultedDict['sigma'])

    def test_ifNotValidSigmaThenModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['sigma'] = 'MySigma'
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.SIGMA, resultedDict['sigma'])

    def test_ifValidL1ThenNotModified(self):
        # setup
        copyDict = dictParameters.copy()
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        self.assertEqual(copyDict['l1'], resultedDict['l1'])

    def test_ifLowerL1ThenModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['l1'] = NegotiationParameters.Constants.L1//2-1
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.L1//2, resultedDict['l1'])

    def test_ifNotValidL1ThenModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['l1'] = 'MyL1'
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.L1, resultedDict['l1'])


    def test_ifValidL2ThenNotModified(self):
        # setup
        copyDict = dictParameters.copy()
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        self.assertEqual(copyDict['l2'], resultedDict['l2'])

    def test_ifLowerL2ThenModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['l2'] = NegotiationParameters.Constants.L2-1
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.L2, resultedDict['l2'])

    def test_ifNotValidL2ThenModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['l2'] = 'MyL2'
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.L2, resultedDict['l2'])


    def test_ifValidWThenNotModified(self):
        # setup
        copyDict = dictParameters.copy()
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        self.assertEqual(copyDict['w'], resultedDict['w'])

    def test_ifLowerWThenModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['w'] = NegotiationParameters.Constants.W-1
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.W, resultedDict['w'])

    def test_ifNotValidWThenModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['w'] = 'MyW'
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.W, resultedDict['w'])

    def test_ifValidMThenNotModified(self):
        # setup
        copyDict = dictParameters.copy()
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        self.assertEqual(copyDict['m'], resultedDict['m'])

    def test_ifLowerMThenModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['m'] = 0.01
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.mMin*resultedDict['lenDataset'], resultedDict['m'])

    def test_ifHigherMThenModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['m'] = 100
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.mMax*resultedDict['lenDataset'], resultedDict['m'])

    def test_ifNotValidMThenModified(self):
        # setup
        copyDict = dictParameters.copy()
        copyDict['m'] = 'MyM'
        # execute
        resultedDict = self.negotiateParametersUtils.validateParameters(copyDict)
        # verify
        print(resultedDict)
        self.assertEqual(NegotiationParameters.Constants.m*resultedDict['lenDataset'], resultedDict['m'])






