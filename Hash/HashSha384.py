from Hash.HashFunction import HashFunction
import hashlib


class HashSha384(HashFunction):
    def initialize(self):
        self._hash = hashlib.sha384()

    def displayResult(self):
        print('Hashed function with SHA384:' + str(self._result))