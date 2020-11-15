import os

from Crypto.Util.Padding import pad
from aspectlib import Aspect, Proceed

import logging

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, '/LOG/logs.log')
logging.basicConfig(filename='CONFIG_PATH', level=logging.DEBUG)

@Aspect
def changePlaintextValidity(*args):
    plaintext = args[1]
    classInstance = args[0]
    blockSize = classInstance.getAlgorithm().block_size

    if isinstance(plaintext, str):
        plaintext = plaintext.encode("utf-8")
    else:
        plaintext = pad(plaintext, blockSize)
    plaintext = pad(plaintext, blockSize)

    yield Proceed(classInstance, plaintext)


@Aspect
def logCipherDetailsErrors(*args):
    classInstance = args[0]
    blockSize = classInstance.getAlgorithm().block_size
    key = classInstance._key
    iv = classInstance._iv

    if not isinstance(key, bytes):
        logging.error('The prf cannot be instantiated with a key of invalid type')
        raise TypeError('Please instantiate your PRF function with a key of byte type')

    if not isinstance(iv, bytes):
        logging.error('The prf was instantiated with an invalid iv')
        raise TypeError('Please instantiate your PRF function with an initialization vector of byte type')

    if len(key) != blockSize:
        logging.error('The prf was instantiated with a key of invalid length')
        raise TypeError('Please instantiate your PRF function with a key of length: ' + str(blockSize))

    if len(iv) != blockSize:
        logging.error('The prf was instantiated with an initialization vector of invalid length')
        raise TypeError('Please instantiate your PRF function with an initialization vector  of length: ' + str(blockSize))

    try:
        yield
    except Exception as exception:
        print('An error has occurred when setting your PRF cipher, please check you logs file for more information')
        logging.error(exception)


@Aspect
def checkHashPlaintextValidity(*args):
    plaintext = args[1]
    classInstance = args[0]

    if isinstance(plaintext, str):
        logging.info('The input has changed so it can be hashed')
        plaintext = plaintext.encode('utf-8')
    elif not isinstance(plaintext, bytes):
        logging.error('Input of invalid type and it can not be hashed')
        raise ValueError('Your input is of invalid type and it can not be hashed')

    try:
        yield Proceed(classInstance, plaintext)
    except Exception as exception:
        print('An error has occurred when you tried to compute your hash, for more information please check your errors log file')
        logging.error(exception)
