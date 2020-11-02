from Hash.HashFunction import HashFunction
import hashlib

class HashMd5(HashFunction):

    def initialize(self):
        self._hash = hashlib.md5()

    def displayResult(self):
        print('Hashed function with MD5: ' + str(self._result))

