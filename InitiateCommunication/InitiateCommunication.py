import threading
import aspectlib
from CommunicationService.TransferProtocol import TransferProtocol


class InitiateCommunication:

    def __init__(self, transferProtocol: TransferProtocol):
        self.transferProtocol = transferProtocol

    def initiateConnection(self):
        self.transferProtocol.initiateConnection()

    def receiveInitiateConnection(self):
        return self.transferProtocol.receiveInitiateConnection()

    # ok, once we have got received out connection, we spawn a thread to process
    # all server operations. We will do it by using monitors

    def threadDemoProcessor(self):
        yield self.transferProtocol.sendConfirmationInitiateConnection()

    @aspectlib.Aspect
    def threadAspect(self):
        yield
        threading.Thread(target=self.threadDemoProcessor).start()

    def sendConfirmationInitiate(self):
        self.transferProtocol.sendConfirmationInitiateConnection()

    def sendConfirmationInitiateConnection(self):
        with aspectlib.weave(self.sendConfirmationInitiate, self.threadAspect):
            self.sendConfirmationInitiate()


    def receiveConfirmationInitiateConnection(self):
        return self.transferProtocol.receiveConfirmationInitiateConnection()

