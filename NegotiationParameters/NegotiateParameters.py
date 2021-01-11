from CommunicationService.TransferProtocol import TransferProtocol
from NegotiationParameters.NegotiateParametersUtils import NegotiateParametersUtils


class NegociateParameters:

    def __init__(self, transferProtocol: TransferProtocol, negotiateParametersUtils :NegotiateParametersUtils):
        self.transferProtocol=transferProtocol
        self.negotiateParametersUtils=negotiateParametersUtils

    def validateParameters(self, dictParameters):
        return self.negotiateParametersUtils.validateParameters(dictParameters)

    def sendParametersToServer(self, dictParameters):
        self.transferProtocol.sendNegotiateParameters(dictParameters)

    def receiveParametersFromClient(self):
        return self.transferProtocol.receiveNegotiateParameters()

    def sendModifiedParametersToClient(self, dictParameters):
        self.transferProtocol.sendBackNegotiateParameters(dictParameters)

    def receiveModifiedParametersFromServer(self):
        return self.transferProtocol.receiveModifiedNegotiateParameters()