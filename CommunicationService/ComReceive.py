import pickle
from Crypto.Cipher import AES
import aspectlib

from CommunicationService.Communication import Communication


class ComReceive(Communication):

    @aspectlib.Aspect
    def decryptDataAES(self, data, flag):

        if flag == 'NoAES':
            yield aspectlib.Proceed
        else:
            cipher = AES.new(self.aesKey, AES.MODE_CFB, self.aesIV)
            data = cipher.decrypt(data)
            yield aspectlib.Proceed(self, data, flag)

    def processData(self, data, flag):

        data = pickle.loads(data)
        return data

    def receive(self, ipToReceive, portToReceive, HEADERSIZE, sizeOfDgram=16, flag=None):

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

                with aspectlib.weave(self.processData, self.decryptDataAES):
                    return self.processData(data, flag)

