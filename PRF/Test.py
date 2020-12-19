import math

from Crypto.Random import get_random_bytes
from Cryptodome.Cipher import AES

from PRF.DES3PrfCreator import DES3PrfCreator
from PRF.DESPrfCreator import DESPrfCreator
from PRF.AESPrfCreator import AESPrfCreator
#
from PRF.OPRF import computeOPrfValue
from PRF.PrfScopeEnum import PrfScopeEnum
from Utils.DataUtil import convertBytesIntoBits, convertBitsIntoString, convertBinaryToDecimal
#
# key = '12345678'.encode("utf8")
# iv = 'This is a key123'.encode("utf8")
# plaintext = b'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS'


# prfCreator = DESPrfCreator(iv, key)
# result = prfCreator.computePrf(plaintext)
# print(len(result))
# from Crypto.Cipher import DES3
# key = b'sdhbsdhfbsdhfsdfbstyiylk'
# print(len(key))
# iv = 'This is a key123'.encode("utf8")
# plaintext = b'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS'
#
#
# cipher = DES3.new(key, DES3.MODE_CFB)
# plaintext = b'We are no longer the knights who say ni!'
# msg = cipher.iv + cipher.encrypt(plaintext)



# key = b'Sixteen byte keySixteen byte key'
# seed = os.urandom(32)
# cipher = AES.new(seed, AES.MODE_CTR)
# cryptotext = cipher.encrypt(key)
# print(len(cryptotext))
# print(cryptotext)
# for i in range(0, 6):
#     cryptotext = cipher.encrypt(key)
#     print(cryptotext, len(cryptotext))


#AES
# l1 = 256
# key = b'0101010101011111'
# plaintext = b'00000000000000000000000000000000'
# w = 633
# m = 16777216
# v = computeOPrfValue(plaintext, key, l1, w, m, 'AES')
# print('v= ', v)

# plaintext = b'We are no longer the knights who say ni!'
#
# key = get_random_bytes(24)
# iv = 'This is a key123'.encode("utf8")
#
# prfCreator = DES3PrfCreator(iv, key,  PrfScopeEnum.GENERATOR)
# result = prfCreator.computePrf(plaintext)
# print(result, len(result))


l1 = 128
key = b'01010101'
plaintext = b'0000000000000000'
w = 633
m = 16777216
v = computeOPrfValue(plaintext, key, l1, w, m, 'DES')
print('v= ', v)


l1 = 384
key = get_random_bytes(24)
plaintext = b'000000000000000000000000000000000000000000000001'
w = 633
m = 16777216
v = computeOPrfValue(plaintext, key, l1, w, m, 'DES3')
print('v= ', v)
