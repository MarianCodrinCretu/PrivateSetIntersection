
from Hash.HashFunction import HashFunction
import hashlib

class HashSha3_256(HashFunction):
    def initialize(self):
        self._hash = hashlib.sha3_256()

    def displayResult(self):
        print('Hashed function with SHA3_256: ' + str(self._result))


