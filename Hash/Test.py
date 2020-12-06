import _hashlib

from Cryptodome.Util.Padding import pad, unpad

from Hash.HashMd5 import HashMd5
from Hash.HashSha1 import HashSha1
from Hash.HashSha256 import HashSha256
from Hash.HashBlake2b import HashBlake2b
#
from PRF.OPRF import OPRF
from Utils.DataUtil import convertBytesIntoBits, splitTextIntoHalves

# desiredBitLength = 256
# plaintext = 'test'
# # print(type(plaintext))
# testConvert = b"\t\x8fk\xcdF!\xd3s\xca\xdeN\x83&'\xb4\xf6"
# print(type(testConvert))
# convertBytesIntoBits(plaintext)
# print(testConvert.decode("utf-8"))
# oprf = OPRF()
# result = oprf.computeOprfValue(testConvert)
# print(result)

# splitResult = splitTextIntoHalves(result)
# print(splitResult)

# print(plaintext)
# md5Hash = HashMd5(128)
# result = md5Hash.generate(plaintext)
# print(len(result))
# for index in range(0, len(result)):
#     print(result[index])
# #
# sha1Hash = HashSha1()
# sha1Hash.generate(plaintext)
#
# blake2bHash = HashBlake2b()
# result = blake2bHash.generate(plaintext)

# #
# sha256Hash = HashSha256(desiredBitLength)
# result = sha256Hash.generate(plaintext)
# print('result', result)
# paddedResult = pad(result, desiredBitLength)
# print(paddedResult)
# print(unpad(paddedResult, desiredBitLength))
# print('test0', len(paddedResult))

# print(type(result))
# print(result[0])
# print(result[63])
