from abc import ABC, abstractmethod

from AOP.DataInterceptor import checkHashPlaintextValidity


class HashFunction(ABC):
    def generate(self, plaintext):
        self.initialize()
        self.computeDigest(plaintext)
        self.displayResult()
        return self._result

    @abstractmethod
    def initialize(self):
        pass

    @checkHashPlaintextValidity
    def computeDigest(self, plaintext):
        self._hash.update(plaintext)
        self._result = self._hash.digest()

    @abstractmethod
    def displayResult(self):
        pass

