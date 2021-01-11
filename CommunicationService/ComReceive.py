import pickle

import aspectlib

from CommunicationService.Communication import Communication
from Exceptions.Utils import exceptionDict


class ComReceive(Communication):

    @aspectlib.Aspect
    def decryptDataAES(self, data, aesCipher, flag):
        if flag == 'NoAES':
            yield aspectlib.Proceed
        else:

            data = aesCipher.decrypt(data)

            yield aspectlib.Proceed(self, data, aesCipher, flag)

    @aspectlib.Aspect
    def securityTestingTune(self, data, flag):

        if flag == 'NoAES':
            yield aspectlib.Proceed
        else:
            import os
            with open(os.path.join('aesAnalysis.txt'), 'a') as filex:
                filex.write(str(data))
                filex.write('\n--------------------\n')
                yield aspectlib.Proceed

    def checkForExceptions(self, data, flag):
        if flag != 'NoAES':
            for key in exceptionDict:
                if key in data:
                    raise exceptionDict[key](data.replace(key, ''))

    def processData(self, data, aesCipher, flag):

        data = pickle.loads(data)
        return data

    def securityTesting(self, data, flag):
        pass

    def receive(self, ipToReceive, portToReceive, HEADERSIZE, aesCipher=None, sizeOfDgram=16, flag=None):

        socket = self._socketPool.acquire()
        socket.bind((ipToReceive, int(portToReceive)))
        socket.listen(5)

        connection, address = socket.accept()

        receivedObject = b''
        newMessage = True
        msglen = 0
        while (True):
            msg = connection.recv(sizeOfDgram)
            if newMessage:
                msglen = int(msg[:HEADERSIZE])
                newMessage = False

            receivedObject += msg

            if len(receivedObject) - HEADERSIZE == msglen:
                self._socketPool.release(socket)
                data = receivedObject[HEADERSIZE:]

                # with aspectlib.weave(self.securityTesting, self.securityTestingTune):
                #     self.securityTesting(data, flag)

                with aspectlib.weave(self.processData, self.decryptDataAES):
                    data = self.processData(data, aesCipher, flag)
                    #self.checkForExceptions(data, flag)
                    return data
