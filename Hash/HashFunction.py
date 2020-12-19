from abc import ABC, abstractmethod

from AOP.DataInterceptor import checkHashPlaintextValidity
from MOP.HashOutputInterceptor import addPaddingToTheOutput


class HashFunction(ABC):
    def __init__(self, l1):
        self._desiredOutputByteLength = l1

    def generate(self, plaintext):
        self.initialize()
        self.computeDigest(plaintext)
        self.displayResult()
        return self._result

    @abstractmethod
    def initialize(self):
        pass

    @addPaddingToTheOutput
    @checkHashPlaintextValidity
    def computeDigest(self, plaintext):
        self._hash.update(plaintext)
        self._result = self._hash.digest()

    @abstractmethod
    def displayResult(self):
        pass
