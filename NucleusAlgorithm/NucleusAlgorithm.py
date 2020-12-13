from OPRFEvaluation.OPRFEvaluation import OPRFEvaluation
from NegotiationParameters.NegotiateParameters import NegociateParameters

from Hash.HashMd5 import HashMd5
from Hash.HashSha256 import HashSha256
from Hash.HashSha1 import HashSha1
from Hash.HashBlake2b import HashBlake2b
from PRF.OPRF import computeOPrfValue

class NucleusAlgorithm:

    def __init__(self, dictParameters, negotiateParameters: NegociateParameters, oprfEvaluation: OPRFEvaluation):
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
        pass

    def senderAlgorithmSide(self):
        pass

