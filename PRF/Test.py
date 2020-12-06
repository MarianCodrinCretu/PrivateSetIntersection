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


# t = 6
# for index in range(0, t + 1):
#     extendedKey += prg.encrypt(key)
# print(extendedKey)
# print(len(extendedKey) == (t+1) * len(key))

# x = b'0'
# y = b'1'
# result = b''
# result += bytes(int(x) ^ int(y))
# print(result)


# seed = os.urandom(16)
# # cryptotextConverted = convertBytesIntoBits(cryptotext)
# print(seed, len(seed))

# from Crypto.Util.Padding import pad
# key = b'010101010101101010101010101010101010110011'
# iv = pad(b"010101010101101010101010101010101010110011", 8)
# # plaintext = pad(b"test ", 8)
# plaintext = b'010101010101101010101010101010101010110011'
# prfCreator = DESPrfCreator(iv, key)
# result = prfCreator.computePrf(plaintext)
# print(len(result))


# t=23234234
#
# print(math.log2(t)//4)
#
# import os
# key=b'00110001001100100011001100110100001101010011011000110111001110000011000100110010001100110011010000110101001101100011011100111000'
# seed = os.urandom(16)
#
#
# cipher = AES.new(seed, AES.MODE_CTR)
# cryptotext = cipher.encrypt(key)
# print(len(cryptotext))

#
l1 = 256
key = b'1234567812345678'
plaintext = b'00000000000000000000000000000000'
w = 633
m = 16777216
v = computeOPrfValue(plaintext, key, l1, w, m, 'AES', False)
print('v= ', v)
# convertBitsIntoString('10110001101010001101011111101101000100010100110111111010110101101101110100111001011010101100110010000100101001110000001001010000')
# print(chr(117))


# def make_bitseq(s: str) -> str:
#      if not s.isascii():
#         raise ValueError("ASCII only allowed")
#      return " ".join(f"{ord(i):08b}" for i in s)
# # print(len(convertBitsIntoString('1010101011111111').encode('utf-8')))
# print(make_bitseq('¨/&#jÃÃ;aoüczæÿ'))


# def make_uchr(code: str):
#     return chr(int(code.lstrip("U+").zfill(8), 16))
#
#
# print(make_uchr('10101000110111101010100011101100101001001010111011111010001110000101001010001010000010010110101001001111001001101100100001100000'))


