from Hash.HashFunction import HashFunction
import hashlib

class HashSha1(HashFunction):
    def initialize(self):
        self._hash = hashlib.sha1()

    def displayResult(self):
        print('Hashed function with SHA1: ' + str(self._result))

