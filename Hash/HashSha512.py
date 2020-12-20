from Hash.HashFunction import HashFunction
import hashlib


class HashSha512(HashFunction):
    def initialize(self):
        self._hash = hashlib.sha512()

    def displayResult(self):
        print('Hashed function with SHA256: ' + str(self._result))


