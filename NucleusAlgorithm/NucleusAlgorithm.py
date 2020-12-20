import Utils.Utils as randomUtils
from Hash.HashBlake2b import HashBlake2b
from Hash.HashMd5 import HashMd5
from Hash.HashSha256 import HashSha256
from Hash.HashSha384 import HashSha384
from Hash.HashSha3_256 import HashSha3_256
from Hash.Sha3_384 import HashSha3_384
from NegotiationParameters.NegotiateParameters import NegociateParameters
from OPRFEvaluation.OPRFEvaluation import OPRFEvaluation
from OTService.OTService import OTService
from PRF.OPRF import computeOPrfValue
from Precomputation.Precomputation import Precomputation


def generateDictFunctions(dictParameters):
    dictFunctions = {}
    if dictParameters['hash1'] == 'MD5':
        dictFunctions['MD5'] = HashMd5(dictParameters['l1'] // 8).generate
    if dictParameters['hash1'] == 'BLAKE2B_16':
        dictFunctions['BLAKE2B_16'] = HashBlake2b(dictParameters['l1'] // 8).generate
    if dictParameters['hash1'] == 'SHA3_256':
        dictFunctions['SHA3_256'] = HashSha3_256(dictParameters['l1'] // 8).generate
    if dictParameters['hash1'] == 'SHA256':
        dictFunctions['SHA256'] = HashSha256(dictParameters['l1'] // 8).generate
    if dictParameters['hash1'] == 'BLAKE2B_32':
        dictFunctions['BLAKE2B_32'] = HashBlake2b(dictParameters['l1'] // 8).generate
    if dictParameters['hash1'] == 'BLAKE2B_48':
        dictFunctions['BLAKE2B_48'] = HashBlake2b(dictParameters['l1'] // 8).generate
    if dictParameters['hash1'] == 'SHA384':
        dictFunctions['SHA384'] = HashSha384(dictParameters['l1'] // 8).generate
    if dictParameters['hash1'] == 'SHA3_384':
        dictFunctions['SHA3_384'] = HashSha3_384(dictParameters['l1'] // 8).generate

    if dictParameters['hash2'] == 'MD5':
        dictFunctions['MD5'] = HashMd5(dictParameters['l2'] // 8).generate
    if dictParameters['hash2'] == 'BLAKE2B_16':
        dictFunctions['BLAKE2B_16'] = HashBlake2b(dictParameters['l2'] // 8).generate
    if dictParameters['hash2'] == 'SHA3_256':
        dictFunctions['SHA3_256'] = HashSha3_256(dictParameters['l2'] // 8).generate
    if dictParameters['hash2'] == 'SHA256':
        dictFunctions['SHA256'] = HashSha256(dictParameters['l2'] // 8).generate
    if dictParameters['hash2'] == 'BLAKE2B_32':
        dictFunctions['BLAKE2B_32'] = HashBlake2b(dictParameters['l2'] // 8).generate
    if dictParameters['hash2'] == 'BLAKE2B_48':
        dictFunctions['BLAKE2B_48'] = HashBlake2b(dictParameters['l2'] // 8).generate
    if dictParameters['hash2'] == 'SHA384':
        dictFunctions['SHA384'] = HashSha384(dictParameters['l2'] // 8).generate
    if dictParameters['hash2'] == 'SHA3_384':
        dictFunctions['SHA3_384'] = HashSha3_384(dictParameters['l2'] // 8).generate

    dictFunctions['FK'] = computeOPrfValue

    return dictFunctions


class NucleusAlgorithm:

    def __init__(self, data, dictParameters,
                 negotiateParameters: NegociateParameters,
                 precomputation: Precomputation,
                 otService: OTService,
                 oprfEvaluation: OPRFEvaluation):
        self.data = data
        self.dictParameters = dictParameters
        self.negotiateParameters = negotiateParameters
        self.precomputation = precomputation
        self.otService = otService
        self.oprfEvaluation = oprfEvaluation

    def receiverAlgorithmSide(self):
        # negociation parameters side
        self.negotiateParameters.sendParametersToServer(self.dictParameters)
        modifiedDict = self.negotiateParameters.receiveModifiedParametersFromServer()

        print(modifiedDict)

        dictFunctions = generateDictFunctions(modifiedDict)

        # precomputation side
        # ---------------------- TO BE COMPLETED -------------------------

        D = randomUtils.RandomUtils.initMatrixDReceiver(modifiedDict['m'], modifiedDict['w'])
        key = randomUtils.RandomUtils.generateKey(modifiedDict['lambda']//8)
        vList = self.precomputation.compute_v_list(self.data, key, modifiedDict, dictFunctions[modifiedDict['hash1']],
                                                   dictFunctions['FK'])
        print(vList)
        D = self.precomputation.update_d(vList, D)

        # ot
        # ---------------------- TO BE COMPLETED -------------------------
        A = randomUtils.RandomUtils.initMatrixAReceiver(modifiedDict['m'], modifiedDict['w'])
        B = randomUtils.PSIAlgoUtils.computeBReceiver(A, D)

        if (modifiedDict['otVariant']) == 1:
            self.otService.receiverOT(A, B, modifiedDict['w'], modifiedDict['m'])
        else:
            self.otService.receiver_randomOT(A, B, modifiedDict['w'], modifiedDict['m'])

        # oprf evaluation
        self.oprfEvaluation.sendKeyToSender(key)
        senderPsiValues = self.oprfEvaluation.receiveSenderPsiValues()
        result = self.oprfEvaluation.evaluatePsiValues(key, senderPsiValues, A, self.data, modifiedDict,
                                                       dictFunctions[modifiedDict['hash1']],
                                                       dictFunctions[modifiedDict['hash2']],
                                                       dictFunctions['FK'])

        return result

    def senderAlgorithmSide(self):
        # negociation parameters side
        receivedDict = self.negotiateParameters.receiveParametersFromClient()
        modifiedDict = self.negotiateParameters.validateParameters(receivedDict)

        print(modifiedDict)
        dictFunctions = generateDictFunctions(modifiedDict)
        self.negotiateParameters.sendModifiedParametersToClient(modifiedDict)

        # precomputation side
        # ---------------------- TO BE COMPLETED -------------------------
        s = randomUtils.RandomUtils.generateSSender(receivedDict['w'])

        # ot
        # ---------------------- TO BE COMPLETED -------------------------
        if (modifiedDict['otVariant']) == 1:
            C = self.otService.senderOT(s, modifiedDict['w'], modifiedDict['m'])
        else:
            C = self.otService.sender_randomOT(s, modifiedDict['w'], modifiedDict['m'])

        # oprf evaluation
        key = self.oprfEvaluation.receiveKeyFromReceiver()
        print(key)
        senderPsiValues = self.oprfEvaluation.generateSenderPsiValues(key, C, self.data, modifiedDict,
                                                                      dictFunctions[modifiedDict['hash1']],
                                                                      dictFunctions[modifiedDict['hash2']],
                                                                      dictFunctions['FK'])
        self.oprfEvaluation.sendSenderPsiValuesToReceiver(senderPsiValues)
