import random

import CommunicationService.TransferProtocol


class OPRFEvaluation:

    def __init__(self, transferProtocol : CommunicationService.TransferProtocol,
                 dictParameters,
                 dictFunctions,
                 data,
                 matrix):

        self.transferProtocol = transferProtocol
        self.dictParameters = dictParameters
        self.dictFunctions=dictFunctions
        self.data=data,
        #matrix = A, if entity=Receiver, else matrix=B for entity=Sender
        self.matrix=matrix

    def computeHash1(self, x):
        return self.dictFunctions[self.dictParameters['hash1']](x)

    def computeHash2(self, x):
        return self.dictFunctions[self.dictParameters['hash2']](x)

    def computePRF(self, x, key):
        return self.dictFunctions['FK'](x, key, self.dictParameters['l1'],
                                        self.dictParameters['w'],
                                        self.dictParameters['m'],
                                        self.dictParameters['prf'])

    def generateKey(self):
        lambdaP = self.dictParameters['lambda']
        key = ""
        for counter in range(lambdaP):
            key+= str(random.randint(0,1))

        return key.encode('utf8')

    def sendKeyToSender(self, key):
        # here, key is a string
        self.transferProtocol.sendPRFKey(key)

    def receiveKeyFromReceiver(self):
        # here, key is a string
        return self.transferProtocol.receiveKey()

    def generateSenderPsiValues(self, key):
        psiSenderList = []

        # self.matrix = C (for sender)
        for x in self.data:
            v = self.computePRF(self.computeHash1(x), key)

            psiDigest = ""

            for counter in range(self.dictParameters['w']):
                intermediary = self.matrix[v[counter]][counter]

                #to see in which form the psiDigest is computed
                psiDigest += str(intermediary)

            psiHash = self.computeHash2(psiDigest)
            psiSenderList.append(psiHash)

        return psiSenderList

    def sendSenderPsiValuesToReceiver(self, psiSenderList):

        self.transferProtocol.sendPsiValues(psiSenderList)

    def receiveSenderPsiValues(self):
        # receive psi values from the sender
        return self.transferProtocol.receivePsiValues()

    def evaluatePsiValues(self, key, senderPsiValues):
        result = []

        #self.matrix = A (for receiver)
        #here is the data from Receiver
        for y in self.data:
            v = self.computePRF(self.computeHash1(y), key)

            psiDigest = ""

            for counter in range(self.dictParameters['w']):
                intermediary = self.matrix[v[counter]][counter]
                psiDigest += str(intermediary)

            # to see in which form the psiDigest is computed
            psiHash = self.computeHash2(psiDigest)

            #checkingEquality
            if psiHash in senderPsiValues:
                result.append(y)

        return result
