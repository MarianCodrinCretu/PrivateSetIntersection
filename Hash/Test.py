
from Hash.HashMd5 import HashMd5
from Hash.HashSha1 import HashSha1
from Hash.HashSha256 import HashSha256
from Hash.HashBlake2b import HashBlake2b
from Hash.HashSha384 import HashSha384
from Hash.HashSha3_256 import HashSha3_256
from Hash.HashSha512 import HashSha512
from Hash.Sha3_384 import HashSha3_384
from Hash.Sha3_512 import HashSha3_512

plaintext='jhdgsjdfb'

blake2bHashRandomResultFrom1To64 = HashBlake2b(2)
result = blake2bHashRandomResultFrom1To64.generate(plaintext)
# print(result, len(result))

blake2bHash64BytesResult = HashBlake2b(64)
result = blake2bHash64BytesResult.generate(plaintext)
# print(result, len(result))

sha1Hash = HashSha1(20)
result = sha1Hash.generate(plaintext)
# print(result, len(result))

sha256Hash = HashSha256(32)
result = sha256Hash.generate(plaintext)
# print(result, len(result))

sha384Hash = HashSha384(48)
result = sha384Hash.generate(plaintext)
# print(result, len(result))


sha512Hash = HashSha512(64)
result = sha512Hash.generate(plaintext)
# print(result, len(result))


md5Hash = HashMd5(16)
result = md5Hash.generate(plaintext)
# print(result, len(result))

sha3_256Hash = HashSha3_256(32)
result = sha3_256Hash.generate(plaintext)
# print(result, len(result))

sha3_384Hash = HashSha3_384(48)
result = sha3_384Hash.generate(plaintext)
# print(result, len(result))

sha3_512Hash = HashSha3_512(64)
result = sha3_512Hash.generate(plaintext)
# print(result, len(result))

