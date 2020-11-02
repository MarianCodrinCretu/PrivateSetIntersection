from Hash.HashFunction import HashFunction
import hashlib

class HashSha256(HashFunction):
    def initialize(self):
        self._hash = hashlib.sha256()

    def displayResult(self):
        print('Hashed function with SHA256: ' + str(self._result))


