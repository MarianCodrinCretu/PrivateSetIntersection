from OPRFEvaluation.OPRFEvaluation import OPRFEvaluation
from NegotiationParameters.NegotiateParameters import NegociateParameters

from Hash.HashMd5 import HashMd5
from Hash.HashSha256 import HashSha256
from Hash.HashSha1 import HashSha1
from Hash.HashBlake2b import HashBlake2b
from PRF.OPRF import computeOPrfValue

class NucleusAlgorithm:

    def __init__(self, data, dictParameters, negotiateParameters: NegociateParameters, oprfEvaluation: OPRFEvaluation):
        self.data=data
        self.dictParameters=dictParameters
        self.negotiateParameters=negotiateParameters
        self.oprfEvaluation=oprfEvaluation

    @staticmethod
    def generateDictFunctions():
        return {
            'MD5': HashMd5().generate,
            'SHA1': HashSha1().generate,
            'SHA256': HashSha256().generate,
            'BLAKE2B' : HashBlake2b().generate,
            'FK': computeOPrfValue
        }

    def receiverAlgorithmSide(self):
        #negociation parameters side
        self.negotiateParameters.sendParametersToServer(self.dictParameters)
        modifiedDict = self.negotiateParameters.receiveModifiedParametersFromServer()

        #precomputation side
        # ---------------------- TO BE COMPLETED -------------------------
        matrix=[]

        # ot
        # ---------------------- TO BE COMPLETED -------------------------

        #oprf evaluation
        key = self.oprfEvaluation.generateKey(modifiedDict)
        self.oprfEvaluation.sendKeyToSender(key)
        senderPsiValues = self.oprfEvaluation.receiveSenderPsiValues()
        result = self.oprfEvaluation.evaluatePsiValues(key, senderPsiValues, matrix, self.data, modifiedDict)

        return result





    def senderAlgorithmSide(self):
        #negociation parameters side
        receivedDict = self.negotiateParameters.receiveParametersFromClient()
        modifiedDict = self.negotiateParameters.validateParameters(receivedDict)
        self.negotiateParameters.sendModifiedParametersToClient(modifiedDict)

        #precomputation side
        # ---------------------- TO BE COMPLETED -------------------------
        matrix = []

        #ot
        # ---------------------- TO BE COMPLETED -------------------------

        #oprf evaluation
        key = self.oprfEvaluation.receiveKeyFromReceiver()
        senderPsiValues=self.oprfEvaluation.generateSenderPsiValues(key, matrix, self.data, modifiedDict)
        self.oprfEvaluation.sendSenderPsiValuesToReceiver(senderPsiValues)



