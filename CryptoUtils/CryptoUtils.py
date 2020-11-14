import os
import random

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import string

def generateClientRSAKeys():

    if (not os.path.isfile('client_rsa_public.pem') and not os.path.isfile('client_rsa_private.pem')):
        key = RSA.generate(4096)
        f = open('client_rsa_public.pem', 'wb')
        f.write(key.publickey().exportKey('PEM'))
        f.close()
        f = open('client_rsa_private.pem', 'wb')
        f.write(key.exportKey('PEM'))
        f.close()

    pubFile = open('client_rsa_public.pem')
    privFile = open('client_rsa_private.pem')

    pubKey = RSA.importKey(pubFile.read())
    privKey = RSA.importKey(privFile.read())

    return (pubKey, privKey)

def generateServerRSAKeys():

    if (not os.path.isfile('server_rsa_public.pem') and not os.path.isfile('server_rsa_private.pem')):
        key = RSA.generate(4096)
        f = open('server_rsa_public.pem', 'wb')
        f.write(key.publickey().exportKey('PEM'))
        f.close()
        f = open('server_rsa_private.pem', 'wb')
        f.write(key.exportKey('PEM'))
        f.close()

    pubFile = open('server_rsa_public.pem')
    privFile = open('server_rsa_private.pem')

    pubKey = RSA.importKey(pubFile.read())
    privKey = RSA.importKey(privFile.read())

    return (pubKey, privKey)

def generateAESKey():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(16))

def generateAESIv():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(16))

def rsaEncrypt(key, data):
    key = PKCS1_OAEP.new(key)
    return key.encrypt(data)

def rsaDecrypt(key, data):
    key = PKCS1_OAEP.new(key)
    return key.decrypt(data).decode('utf8')

def convertRSAKeyToString(rsaKey):
    return rsaKey.exportKey("PEM")

def stringToRSAKey(stringKey):
    return RSA.importKey(stringKey)


key = generateAESKey()
(publicKey, privateKey) = generateClientRSAKeys()
generateServerRSAKeys()
print(key)
print(rsaDecrypt(privateKey, rsaEncrypt(publicKey, key.encode('utf8'))))

