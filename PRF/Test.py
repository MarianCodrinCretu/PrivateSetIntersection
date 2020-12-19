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



# prfCreator = DESPrfCreator(iv, key)
# result = prfCreator.computePrf(plaintext)
# print(len(result))
# from Crypto.Cipher import DES3
# key = b'sdhbsdhfbsdhfsdfbstyiylk'
# print(len(key))
# iv = 'This is a key123'.encode("utf8")
# plaintext = b'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS'
#

plaintext = b'We are no longer the knights who say ni!'
key = get_random_bytes(24)
iv = 'This is a key123'.encode("utf8")

prfCreator = DES3PrfCreator(iv, key)
result = prfCreator.computePrf(plaintext, PrfScopeEnum.GENERATOR)
print(result, len(result))

# AES
l1 = 256
key = b'0101010101011111'
plaintext = b'00000000000000000000000000000000'
w = 633
m = 16777216
v = computeOPrfValue(plaintext, key, l1, w, m, 'AES')
print('v= ', v)


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
