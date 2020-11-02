from abc import ABC, abstractmethod

class PRFCreator(ABC):
    def __init__(self, iv, key) -> None:
        self._iv = iv
        self._key = key
        self._prf = self.createPrf()

    @abstractmethod
    def  createPrf(self):
       pass

    def computePrf(self, plaintext):
        return self._prf.computePrf(plaintext)





