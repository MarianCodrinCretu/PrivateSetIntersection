import CommunicationService.TransferProtocol


class OPRFEvaluation:

    def __init__(self, transferProtocol: CommunicationService.TransferProtocol):

        self.transferProtocol = transferProtocol
        # matrix = A, if entity=Receiver, else matrix=B for entity=Sender

    def computeHash1(self, x, functionHash1):
        return functionHash1(x)

    def computeHash2(self, x, functionHash2):
        return functionHash2(x)

    def computePRF(self, x, key, dictParameters, functionPRF):
        return functionPRF(x, key, dictParameters['l1'],
                           dictParameters['w'],
                           dictParameters['m'],
                           dictParameters['prf'])

    def sendKeyToSender(self, key):
        # here, key is a string
        self.transferProtocol.sendPRFKey(key)

    def receiveKeyFromReceiver(self):
        # here, key is a string
        return self.transferProtocol.receiveKey()

    def generateSenderPsiValues(self, key, matrix, data, dictParameters, functionHash1, functionHash2, functionPRF):
        psiSenderList = []

        # self.matrix = C (for sender)
        for x in data:
            v = self.computePRF(self.computeHash1(x, functionHash1), key, dictParameters, functionPRF)
            psiDigest = ""

            for counter in range(dictParameters['w']):
                intermediary = matrix[v[counter]][counter]
                # to see in which form the psiDigest is computed
                psiDigest += str(intermediary)

            psiHash = self.computeHash2(psiDigest, functionHash2)
            psiSenderList.append(psiHash)

        return psiSenderList

    def sendSenderPsiValuesToReceiver(self, psiSenderList):

        self.transferProtocol.sendPsiValues(psiSenderList)

    def receiveSenderPsiValues(self):
        # receive psi values from the sender
        return self.transferProtocol.receivePsiValues()

    def evaluatePsiValues(self, key, senderPsiValues, matrix, data, dictParameters, functionHash1, functionHash2,
                          functionPRF):
        result = []
        # self.matrix = A (for receiver)
        # here is the data from Receiver
        for y in data:
            v = self.computePRF(self.computeHash1(y, functionHash1), key, dictParameters, functionPRF)
            psiDigest = ""

            for counter in range(dictParameters['w']):
                intermediary = matrix[v[counter]][counter]
                psiDigest += str(intermediary)

            # to see in which form the psiDigest is computed
            psiHash = self.computeHash2(psiDigest, functionHash2)

            # checkingEquality
            if psiHash in senderPsiValues:
                result.append(y)

        return result
