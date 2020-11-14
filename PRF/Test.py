
from PRF.DESPrfCreator import DESPrfCreator
from PRF.AESPrfCreator import AESPrfCreator
#
# key = 'This is a key123'.encode("utf8")
# iv = 'This is an IV456'.encode("utf8")
# print(type(key))
# plaintext = 'This is a key123'
#
# prfCreator = AESPrfCreator(iv, key)
# result = prfCreator.computePrf(plaintext)
# print(result)

from Crypto.Util.Padding import pad
key = "12345678"
iv = pad(b"Thidd", 8)
# plaintext = pad(b"test ", 8)
plaintext = 'andzddsdfsdfsdfsdfsdfsdfsddsfdsfdsfdsffdfsfsdfsdfssdfsdfsdfsdfsdfsdfsdfsdfsdffsfsdfsdfdfsdfsdfsddsfsdffddfsfdsdfsdfr'
prfCreator = DESPrfCreator(iv, key)
# result = prfCreator.computePrf(plaintext)
# print(isinstance(plaintext, str))

