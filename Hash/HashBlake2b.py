from Hash.HashFunction import HashFunction
import hashlib
import os


class HashBlake2b(HashFunction):
    def initialize(self):
        blakeSalt = os.urandom(hashlib.blake2b.SALT_SIZE)
        blakeSaltString = 'a'*hashlib.blake2b.SALT_SIZE
        blakeSalt = blakeSaltString.encode('utf8')
        self._hash = hashlib.blake2b(salt=blakeSalt,  digest_size=self._desiredOutputByteLength)


    def displayResult(self):
        print('Hashed function with Blake2b with salt: ' + str(self._result))



