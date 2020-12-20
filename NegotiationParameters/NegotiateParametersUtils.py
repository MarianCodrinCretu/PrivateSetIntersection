import NegotiationParameters.Constants
import aspectlib
import logging
from Logs import LogMessaging
logging.basicConfig(filename='../Logs/logs.log', level=logging.DEBUG)

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


class NegotiateParametersUtils:

    @aspectlib.Aspect
    def tunedValidateFirstHashFunction(self, dictParameters):
        lambdax = dictParameters['lambda']
        yield aspectlib.Proceed(self, dictParameters)
        if dictParameters['hash1'].upper() in NegotiationParameters.Constants.HASHES[lambdax]:
            dictParameters['hash1'] = dictParameters['hash1'].upper()
        else:
            dictParameters['hash1'] = NegotiationParameters.Constants.DEFAULT_HASH[lambdax]

    def validateFirstHashFunction(self, dictParameters):
        lambdax = dictParameters['lambda']
        if dictParameters['hash1'].upper() not in NegotiationParameters.Constants.HASHES[lambdax]:
            print('First hash function is not corresponding with lambda '+str(lambdax)+' chosen')
            logging.info(LogMessaging.firstHashWrong(lambdax)[0])

    @aspectlib.Aspect
    def tunedValidateSecondHashFunction(self, dictParameters):
        yield aspectlib.Proceed(self, dictParameters)
        if dictParameters['hash2'].upper() in NegotiationParameters.Constants.HASH_LIST:
            dictParameters['hash2'] = dictParameters['hash2'].upper()
        else:
            dictParameters['hash2'] = NegotiationParameters.Constants.DEFAULT_HASH_SINGLE

    def validateSecondHashFunction(self, dictParameters):
        if dictParameters['hash2'] not in NegotiationParameters.Constants.HASH_LIST:
            print('Second hash function is not valid')
            logging.info(LogMessaging.secondHashWrong()[0])

    @aspectlib.Aspect
    def tunedValidatePRF(self, dictParameters):
        lambdax = dictParameters['lambda']
        yield aspectlib.Proceed(self, dictParameters)
        if dictParameters['prf'].upper() in NegotiationParameters.Constants.PRFS[lambdax]:
            dictParameters['prf'] = dictParameters['prf'].upper()
        else:
            dictParameters['prf'] = NegotiationParameters.Constants.DEFAULT_PRF[lambdax]

    def validatePRF(self, dictParameters):
        lambdax = dictParameters['lambda']
        if dictParameters['prf'] not in NegotiationParameters.Constants.PRFS[lambdax]:
            print('PRF is not valid for '+str(lambdax)+' selected')
            logging.info(LogMessaging.prfWrong(lambdax)[0])

    @aspectlib.Aspect
    def tunedValidateOTVariant(self, dictParameters):
        yield aspectlib.Proceed(self, dictParameters)
        if dictParameters['otVariant'].upper() in NegotiationParameters.Constants.OT_VARIANTS:
            dictParameters['otVariant'] = int(dictParameters['otVariant'])
        else:
            dictParameters['otVariant'] = NegotiationParameters.Constants.DEFAULT_OT

    def validateOTVariant(self, dictParameters):
        if dictParameters['otVariant'] not in NegotiationParameters.Constants.OT_VARIANTS:
            print('OT Variants not valid; please select 1 or 2')
            logging.info(LogMessaging.otVariantWrong()[0])

    @aspectlib.Aspect
    def tunedValidateLambda(self, dictParameters):
        listx = NegotiationParameters.Constants.LAMBDAS
        yield aspectlib.Proceed(self, dictParameters)
        if (isinstance(dictParameters['lambda'], int) or dictParameters['lambda'].isnumeric()):
            if int(dictParameters['lambda']) in listx:
                dictParameters['lambda'] = int(dictParameters['lambda'])
            else:
                dictParameters['lambda'] = NegotiationParameters.Constants.LAMBDA
        else:
            dictParameters['lambda'] = NegotiationParameters.Constants.LAMBDA

    def validateLambda(self, dictParameters):
        listx = NegotiationParameters.Constants.LAMBDAS
        if isinstance(dictParameters['lambda'], int) or dictParameters['lambda'].isnumeric():

            if int(dictParameters['lambda']) not in listx:
                print('Lambda is not an accepted value! Please insert a value from '+str(listx))
                logging.info(LogMessaging.lambdaWrong(listx)[0])

        else:
            print('Invalid lambda')
            logging.info(LogMessaging.lambdaWrong(listx)[0])

    @aspectlib.Aspect
    def tunedValidateSigma(self, dictParameters):
        yield aspectlib.Proceed(self, dictParameters)
        if isinstance(dictParameters['sigma'], int) or dictParameters['sigma'].isnumeric():
            dictParameters['sigma'] = max(NegotiationParameters.Constants.SIGMA, int(dictParameters['sigma']))
        else:
            dictParameters['sigma'] = NegotiationParameters.Constants.SIGMA

    def validateSigma(self, dictParameters):
        if isinstance(dictParameters['sigma'], int) or dictParameters['sigma'].isnumeric():
            if int(dictParameters['sigma']) < NegotiationParameters.Constants.SIGMA:
                print('Sigma too low; please select a value higher than 40')
                logging.info(LogMessaging.sigmaLow()[0])
        else:
            print('Invalid sigma')
            logging.info(LogMessaging.sigmaWrong()[0])

    def validateL1(self, dictParameters):
        dictParameters['l1'] = int(dictParameters['lambda']*2)

    def validateL2(self, dictParameters):
        hash2 = dictParameters['hash2']
        for key in NegotiationParameters.Constants.DEFAULT_HASH:
            if hash2 in NegotiationParameters.Constants.DEFAULT_HASH[key]:
                dictParameters['l2']=2*key
                break


    @aspectlib.Aspect
    def tunedValidateW(self, dictParameters):
        yield aspectlib.Proceed(self, dictParameters)
        if isinstance(dictParameters['w'], int) or dictParameters['w'].isnumeric():
            dictParameters['w'] = max(NegotiationParameters.Constants.W, int(dictParameters['w']))
        else:
            dictParameters['w'] = NegotiationParameters.Constants.W

    def validateW(self, dictParameters):
        if isinstance(dictParameters['w'], int) or dictParameters['w'].isnumeric():
            if int(dictParameters['w']) < NegotiationParameters.Constants.W:
                print('W too low; please select a value higher at least than 10')
                logging.info(LogMessaging.wLow()[0])
        else:
            print('Invalid W')
            logging.info(LogMessaging.wWrong()[0])

    @aspectlib.Aspect
    def tunedValidateM(self, dictParameters):
        yield aspectlib.Proceed(self, dictParameters)
        if isinstance(dictParameters['m'], float) or isfloat(dictParameters['m']):
            dictParameters['m'] = max(NegotiationParameters.Constants.mMin, float(dictParameters['m']))
            if dictParameters['m'] > NegotiationParameters.Constants.mMax:
                dictParameters['m'] = NegotiationParameters.Constants.mMax
        else:
            dictParameters['m'] = NegotiationParameters.Constants.m

        dictParameters['m'] *= dictParameters['lenDataset']
        dictParameters['m']=int(dictParameters['m'])

    def validateM(self, dictParameters):
        if isinstance(dictParameters['m'], float) or isfloat(dictParameters['m']):
            if float(dictParameters['m']) < NegotiationParameters.Constants.mMin \
                    or float(dictParameters['m']) > NegotiationParameters.Constants.mMax:
                print('M not between 0.25 and 1.25')
                logging.info(LogMessaging.mLow()[0])
        else:
            print('Invalid M')
            logging.info(LogMessaging.mWrong()[0])

    def validateParameters(self, dictParameters):

        # lambda validation
        with aspectlib.weave(self.validateLambda, self.tunedValidateLambda):
            self.validateLambda(dictParameters)

        #sigma validation
        with aspectlib.weave(self.validateSigma, self.tunedValidateSigma):
            self.validateSigma(dictParameters)

        #otVariantValidation

        with aspectlib.weave(self.validateOTVariant, self.tunedValidateOTVariant):
            self.validateOTVariant(dictParameters)

        #l1 Validation

        self.validateL1(dictParameters)

        #first Hash validation

        with aspectlib.weave(self.validateFirstHashFunction, self.tunedValidateFirstHashFunction):
            self.validateFirstHashFunction(dictParameters)

        #prf validation
        with aspectlib.weave(self.validatePRF, self.tunedValidatePRF):
            self.validatePRF(dictParameters)

        #second hash validation
        with aspectlib.weave(self.validateSecondHashFunction, self.tunedValidateSecondHashFunction):
            self.validateSecondHashFunction(dictParameters)

        #l2 validation

        self.validateL2(dictParameters)

        # w validation
        with aspectlib.weave(self.validateW, self.tunedValidateW):
            self.validateW(dictParameters)

        # m validation
        with aspectlib.weave(self.validateM, self.tunedValidateM):
            self.validateM(dictParameters)



        return dictParameters
