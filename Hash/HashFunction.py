from abc import ABC, abstractmethod

class HashFunction(ABC):
    def generate(self, plaintext):
        self.initialize()
        self.computeDigest(plaintext)
        self.displayResult()
        return self._result

    @abstractmethod
    def initialize(self):
        pass

    def computeDigest(self, plaintext):
        self._hash.update(plaintext)
        self._result = self._hash.digest()

    @abstractmethod
    def displayResult(self):
        pass

