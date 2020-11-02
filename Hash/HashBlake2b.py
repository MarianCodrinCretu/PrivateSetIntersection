from Hash.HashFunction import HashFunction
import hashlib
import os


class HashBlake2b(HashFunction):

    def initialize(self):
        blakeSalt = os.urandom(hashlib.blake2b.SALT_SIZE)
        self._hash = hashlib.blake2b(salt=blakeSalt)


    def displayResult(self):
        print('Hashed function with Blake2b with salt: ' + str(self._result))



