import math

from Cryptodome.Cipher import AES

from PRF.DESPrfCreator import DESPrfCreator
from PRF.AESPrfCreator import AESPrfCreator
#
from PRF.OPRF import computeOPrfValue
from Utils.DataUtil import convertBytesIntoBits, convertBitsIntoString, convertBinaryToDecimal

# key = 'This is a key123'.encode("utf8")
# iv = 'This is a key123'.encode("utf8")
# plaintext = b'S'

#
# prfCreator = AESPrfCreator(iv, key)
# result = prfCreator.computePrf(plaintext)
# print(len(result))

# key = b'Sixteen byte keySixteen byte key'
# seed = os.urandom(32)
# cipher = AES.new(seed, AES.MODE_CTR)
# cryptotext = cipher.encrypt(key)
# print(len(cryptotext))
# print(cryptotext)
# for i in range(0, 6):
#     cryptotext = cipher.encrypt(key)
#     print(cryptotext, len(cryptotext))

l1 = 256
key = b'1234567812345678'
plaintext = b'00000000000000000000000000000000'
w = 633
m = 16777216
v = computeOPrfValue(plaintext, key, l1, w, m, 'AES', False)
print('v= ', v)


