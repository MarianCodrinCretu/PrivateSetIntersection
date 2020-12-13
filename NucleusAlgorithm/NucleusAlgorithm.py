from OPRFEvaluation.OPRFEvaluation import OPRFEvaluation
from NegotiationParameters.NegotiateParameters import NegociateParameters
from OTService.OTService import OTService
from Precomputation.Precomputation import Precomputation
import Utils.Utils as randomUtils

from Hash.HashMd5 import HashMd5
from Hash.HashSha256 import HashSha256
from Hash.HashSha1 import HashSha1
from Hash.HashBlake2b import HashBlake2b
from PRF.OPRF import computeOPrfValue

class NucleusAlgorithm:

    def __init__(self, data, dictParameters,
                 negotiateParameters: NegociateParameters,
                 precomputation: Precomputation,
                 otService:OTService,
                 oprfEvaluation: OPRFEvaluation):
        self.data=data
        self.dictParameters=dictParameters
        self.negotiateParameters=negotiateParameters
        self.precomputation=precomputation
        self.otService=otService
        self.oprfEvaluation=oprfEvaluation

    @staticmethod
    def generateDictFunctions():
        return {
            'MD5': HashMd5().generate,
            'SHA1': HashSha1().generate,
            'SHA256': HashSha256().generate,
            'BLAKE2B' : HashBlake2b().generate,
            'FK': computeOPrfValue,
        }

    def receiverAlgorithmSide(self):
        #negociation parameters side
        self.negotiateParameters.sendParametersToServer(self.dictParameters)
        modifiedDict = self.negotiateParameters.receiveModifiedParametersFromServer()

        #precomputation side
        # ---------------------- TO BE COMPLETED -------------------------

        D = randomUtils.RandomUtils.initMatrixDReceiver(modifiedDict['m'], modifiedDict['w'])
        key = randomUtils.RandomUtils.generateKey(modifiedDict['lambda'])
        vList=self.precomputation.compute_input(self.data, key, modifiedDict)

        for element in vList:
            D= self.precomputation.update_d(element, D)

        # ot
        # ---------------------- TO BE COMPLETED -------------------------
        A = randomUtils.RandomUtils.initMatrixAReceiver(modifiedDict['m'], modifiedDict['w'])
        B = randomUtils.PSIAlgoUtils.computeBReceiver(A, D)

        if (modifiedDict['otVariant'])==1:
            self.otService.receiverOT(A,B,modifiedDict['w'], modifiedDict['m'])
        else:
            self.otService.receiver_randomOT(A, B, modifiedDict['w'], modifiedDict['m'])

        #oprf evaluation
        self.oprfEvaluation.sendKeyToSender(key)
        senderPsiValues = self.oprfEvaluation.receiveSenderPsiValues()
        result = self.oprfEvaluation.evaluatePsiValues(key, senderPsiValues, A, self.data, modifiedDict)

        return result

    def senderAlgorithmSide(self):
        #negociation parameters side
        receivedDict = self.negotiateParameters.receiveParametersFromClient()
        modifiedDict = self.negotiateParameters.validateParameters(receivedDict)
        self.negotiateParameters.sendModifiedParametersToClient(modifiedDict)

        #precomputation side
        # ---------------------- TO BE COMPLETED -------------------------
        s = randomUtils.RandomUtils.generateSSender(receivedDict['w'])

        #ot
        # ---------------------- TO BE COMPLETED -------------------------
        if (modifiedDict['otVariant'])==1:
            C = self.otService.senderOT(s,modifiedDict['w'], modifiedDict['m'])
        else:
            C = self.otService.senderOT(s, modifiedDict['w'], modifiedDict['m'])

        #oprf evaluation
        key = self.oprfEvaluation.receiveKeyFromReceiver()
        senderPsiValues=self.oprfEvaluation.generateSenderPsiValues(key, C, self.data, modifiedDict)
        self.oprfEvaluation.sendSenderPsiValuesToReceiver(senderPsiValues)



