import NegotiationParameters.Constants
import aspectlib

"""""@author mcretu"""

""" Dictionary form """

''' 
dict = {
    lambda: lambdaValue;
    sigma: sigmaValue;
    m: mValue;
    w: wValue;
    l1: l1Value;
    l2: l2Value;
    hash1: hash1String;
    hash2: hash2String;
    prf: prfString;
    otVariant: otVariant;
    lenDataset: len;
}
'''

''''''

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

class NegociateParametersUtils:

    @aspectlib.Aspect
    def tunedValidateFirstHashFunction(self, dictParameters):
        if dictParameters['hash1'].upper() in NegotiationParameters.Constants.HASH_LIST:
            dictParameters['hash1'] = dictParameters['hash1'].upper()
        else:
            dictParameters['hash1'] = NegotiationParameters.Constants.DEFAULT_HASH

    def validateFirstHashFunction(self, dictParameters):
        if dictParameters['hash1'] not in NegotiationParameters.Constants.HASH_LIST:
            raise Exception('First hash function is not valid')




    @aspectlib.Aspect
    def tunedValidateSecondHashFunction(self, dictParameters):
        if dictParameters['hash2'].upper() in NegotiationParameters.Constants.HASH_LIST:
            dictParameters['hash2'] = dictParameters['hash2'].upper()
        else:
            dictParameters['hash2'] = NegotiationParameters.Constants.DEFAULT_HASH

    def validateSecondHashFunction(self, dictParameters):
        if dictParameters['hash2'] not in NegotiationParameters.Constants.HASH_LIST:
            raise Exception('Second hash function is not valid')




    @aspectlib.Aspect
    def tunedValidatePRF(self, dictParameters):
        if dictParameters['prf'].upper() in NegotiationParameters.Constants.HASH_LIST:
            dictParameters['prf'] = dictParameters['prf'].upper()
        else:
            dictParameters['prf'] = NegotiationParameters.Constants.DEFAULT_PRF

    def validatePRF(self, dictParameters):
        if dictParameters['prf'] not in NegotiationParameters.Constants.PRF_LIST:
            raise Exception('PRF is not valid')



    @aspectlib.Aspect
    def tunedValidateOTVariant(self, dictParameters):
        if dictParameters['otVariant'].upper() in NegotiationParameters.Constants.OT_VARIANTS:
            dictParameters['otVariant'] = int(dictParameters['otVariant'])
        else:
            dictParameters['otVariant'] = NegotiationParameters.Constants.DEFAULT_OT

    def validateOTVariant(self, dictParameters):
        if dictParameters['otVariant'] not in NegotiationParameters.Constants.OT_VARIANTS:
            raise Exception('OT Variants not valid; please select 1 or 2')

    @aspectlib.Aspect
    def tunedValidateLambda(self, dictParameters):
        if isinstance(dictParameters['lambda'], int) or dictParameters['lambda'].isnumeric():
            dictParameters['lambda'] = max(NegotiationParameters.Constants.LAMBDA, int(dictParameters['lambda']))
        else:
            dictParameters['lambda'] = NegotiationParameters.Constants.LAMBDA

    def validateLambda(self, dictParameters):
        if isinstance(dictParameters['lambda'], int) or dictParameters['lambda'].isnumeric():
            if int(dictParameters['lambda']) < NegotiationParameters.Constants.LAMBDA:
                raise Exception('Lambda too low; please select a value higher than 128')
        else:
            raise Exception('Invalid lambda')



    @aspectlib.Aspect
    def tunedValidateSigma(self, dictParameters):
        if isinstance(dictParameters['sigma'], int) or dictParameters['sigma'].isnumeric():
            dictParameters['sigma'] = max(NegotiationParameters.Constants.SIGMA, int(dictParameters['sigma']))
        else:
            dictParameters['sigma'] = NegotiationParameters.Constants.SIGMA

    def validateSigma(self, dictParameters):
        if isinstance(dictParameters['sigma'], int) or dictParameters['sigma'].isnumeric():
            if int(dictParameters['sigma']) < NegotiationParameters.Constants.SIGMA:
                raise Exception('Sigma too low; please select a value higher than 40')
        else:
            raise Exception('Invalid sigma')



    @aspectlib.Aspect
    def tunedValidateL1(self, dictParameters):
        if isinstance(dictParameters['l1'], int) or dictParameters['l1'].isnumeric():
            dictParameters['l1'] = max(NegotiationParameters.Constants.L1 / 2, int(dictParameters['l1']))
        else:
            dictParameters['l1'] = NegotiationParameters.Constants.L1

    def validateL1(self, dictParameters):
        if isinstance(dictParameters['l1'], int) or dictParameters['l1'].isnumeric():
            if int(dictParameters['l1']) < NegotiationParameters.Constants.L1/2:
                raise Exception('L1 too low; please select a value higher than 128')
        else:
            raise Exception('Invalid L1')


    @aspectlib.Aspect
    def tunedValidateL2(self, dictParameters):
        if isinstance(dictParameters['l2'], int) or dictParameters['l2'].isnumeric():
            dictParameters['l2'] = max(NegotiationParameters.Constants.L2, int(dictParameters['l2']))
        else:
            dictParameters['l2'] = NegotiationParameters.Constants.L2

    def validateL2(self, dictParameters):
        if isinstance(dictParameters['l2'], int) or dictParameters['l2'].isnumeric():
            if int(dictParameters['l2']) < NegotiationParameters.Constants.L2:
                raise Exception('L2 too low; please select a value higher than 50')
        else:
            raise Exception('Invalid L2')

    @aspectlib.Aspect
    def tunedValidateW(self, dictParameters):
        if isinstance(dictParameters['w'], int) or dictParameters['w'].isnumeric():
            dictParameters['w'] = max(NegotiationParameters.Constants.W, int(dictParameters['w']))
        else:
            dictParameters['w'] = NegotiationParameters.Constants.W

    def validateW(self, dictParameters):
        if isinstance(dictParameters['w'], int) or dictParameters['w'].isnumeric():
            if int(dictParameters['w']) < NegotiationParameters.Constants.W:
                raise Exception('W too low; please select a value higher at least than 10')
        else:
            raise Exception('Invalid sigma')


    @aspectlib.Aspect
    def tunedValidateM(self, dictParameters):
        if isinstance(dictParameters['m'], float) or isfloat(dictParameters['m']):
            dictParameters['m'] = max(NegotiationParameters.Constants.mMin, float(dictParameters['m']))
            if dictParameters['m'] > NegotiationParameters.Constants.mMax:
                dictParameters['m']=NegotiationParameters.Constants.mMax
        else:
            dictParameters['m'] = NegotiationParameters.Constants.m

        dictParameters['m'] *= dictParameters['lenDataset']

    def validateM(self, dictParameters):
        if isinstance(dictParameters['m'], float) or isfloat(dictParameters['m']):
            if float(dictParameters['m'])< NegotiationParameters.Constants.mMin \
                    or float(dictParameters['m']) > NegotiationParameters.Constants.mMax:
                raise Exception('M not between 0.25 and 1.25')
        else:
            raise Exception('Invalid M')

        dictParameters['m'] *= dictParameters['lenDataset']

    def validateParameters(self, dictParameters):

        with aspectlib.weave(self.tunedValidateFirstHashFunction, self.validateFirstHashFunction):
            self.validateFirstHashFunction(dictParameters)

        with aspectlib.weave(self.tunedValidateSecondHashFunction, self.validateSecondHashFunction):
            self.validateSecondHashFunction(dictParameters)

        with aspectlib.weave(self.tunedValidatePRF, self.validatePRF):
            self.validatePRF(dictParameters)

        with aspectlib.weave(self.tunedValidateOTVariant, self.validateOTVariant):
            self.validateOTVariant(dictParameters)

        with aspectlib.weave(self.tunedValidateLambda, self.validateLambda):
            self.validateLambda(dictParameters)

        with aspectlib.weave(self.tunedValidateSigma, self.validateSigma):
            self.validateSigma(dictParameters)

        with aspectlib.weave(self.tunedValidateL1, self.validateL1):
            self.validateL1(dictParameters)

        with aspectlib.weave(self.tunedValidateL2, self.validateL2):
            self.validateL2(dictParameters)

        with aspectlib.weave(self.tunedValidateM, self.validateM):
            self.validateM(dictParameters)

        with aspectlib.weave(self.tunedValidateW, self.validateW):
            self.validateW(dictParameters)

        return dictParameters






