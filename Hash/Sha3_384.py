from Hash.HashFunction import HashFunction
import hashlib


class HashSha3_384(HashFunction):
    def initialize(self):
        self._hash = hashlib.sha3_384()

    def displayResult(self):
        print('Hashed function with SHA3_384: ' + str(self._result))