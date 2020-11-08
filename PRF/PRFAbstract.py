from abc import ABC


class PRFAbstract(ABC):
    def __init__(self, iv, key):
        self._iv = iv
        self._key = key
        self.setCipher()


    def computePrf(self, plaintext):
        raise NotImplementedError()

    def setCipher(self):
        raise NotImplementedError()
