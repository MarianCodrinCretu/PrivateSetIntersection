from Crypto.Random import get_random_bytes
from PRF.OPRF import computeOPrfValue
from PRF.PRFCreator import PRFCreator
from Shared.Enums.PrfScopeEnum import PrfScopeEnum
from Shared.Enums.PrfTypeEnum import PrfTypeEnum


key = get_random_bytes(8)
plaintext = b'We are no longer'
prfCreator = PRFCreator(PrfTypeEnum.DES, key)
result = prfCreator.computePrf(plaintext, PrfScopeEnum.PRG)
print('Result of encryption with DES:', result, len(result))

#AES
plaintext = b'We are no longer'
key = get_random_bytes(16)
prfCreator = PRFCreator(PrfTypeEnum.AES, key)
result = prfCreator.computePrf(plaintext, PrfScopeEnum.GENERATOR)
print('Result of encryption with AES:', result, len(result))

#DES3
plaintext = b'We are no longer the knights who say ni!'
key = get_random_bytes(24)
iv = 'This is a key123'.encode("utf8")
prfCreator = PRFCreator(PrfTypeEnum.DES3, key, iv)
result = prfCreator.computePrf(plaintext, PrfScopeEnum.GENERIC)
print('Result of encryption with DES3:', result, len(result))

# AES
l1 = 256
key = b'0101010101011111'
plaintext = b'00000000000000000000000000000000'
w = 633
m = 16777216
v = computeOPrfValue(plaintext, key, l1, w, m, 'AES')
print('v= ', v)

#DES
l1 = 128
key = b'01010101'
plaintext = b'0000000000000000'
w = 633
m = 16777216
v = computeOPrfValue(plaintext, key, l1, w, m, 'DES')
print('v= ', v)

#DES3
l1 = 384
key = get_random_bytes(24)
plaintext = b'000000000000000000000000000000000000000000000001'
w = 633
m = 16777216
v = computeOPrfValue(plaintext, key, l1, w, m, 'DES3')
print('v= ', v)



