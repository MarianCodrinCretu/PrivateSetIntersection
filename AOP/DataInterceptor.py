from Crypto.Cipher import DES3
from aspectlib import Aspect, Proceed
from datetime import datetime

import logging


# logging.basicConfig(filename='../LOG/logs.log', level=logging.DEBUG)


@Aspect
def changePlaintextValidity(classInstance, plaintext, scope):

    if isinstance(plaintext, str):
        plaintext = plaintext.encode("utf-8")
        loggingInfo = '[ ' + getCurrentTime() + ' ] The plaintext type has been changed to bytes so it can be computed'
        logging.info(loggingInfo)
        # raise TypeError('The prf cannot be computed on this type of value')
    elif not isinstance(plaintext, bytes):
        loggingError = '[ ' + getCurrentTime() + ' ] The prf cannot be computed on this type of value' + str(type(plaintext))
        logging.error(loggingError)
        # raise TypeError('The prf cannot be computed on this type of value')

    yield Proceed(classInstance, plaintext, scope)


@Aspect
def logCipherDetailsErrors(classInstance):
    blockSize = getBlockSize(classInstance)
    key = classInstance._key
    iv = classInstance._iv

    if not isinstance(key, bytes):
        loggingError = '[ ' + getCurrentTime() + ' ] The prf cannot be instantiated with a key of invalid type'
        logging.error(loggingError)
        raise TypeError('Please instantiate your PRF function with a key of byte type')

    if not isinstance(iv, bytes):
        loggingError = '[ ' + getCurrentTime() + ' ] The prf was instantiated with an invalid iv'
        logging.error(loggingError)
        raise TypeError('Please instantiate your PRF function with an initialization vector of byte type')

    if len(key) != getBlockSize(classInstance):
        loggingError = '[ ' + getCurrentTime() + ' ] The prf was instantiated with a key of invalid length'
        logging.error(loggingError)
        raise TypeError('Please instantiate your PRF function with a key of length: ' + str(blockSize))

    try:
        yield
    except Exception as exception:
        print('An error has occurred when setting your PRF cipher, please check you logs file for more information')
        loggingError = '[ ' + getCurrentTime() + ' ] ' + str(exception)
        logging.error(loggingError)

def getBlockSize(classInstance):
    blockSize = classInstance.getAlgorithm().block_size

    if classInstance.getAlgorithm() == DES3:
        blockSize = 24
    return blockSize

@Aspect
def checkHashPlaintextValidity(*args):
    plaintext = args[1]
    classInstance = args[0]

    if isinstance(plaintext, str):
        loggingInfo = '[ ' + getCurrentTime() + ' ] The input has changed so it can be hashed'
        logging.info(loggingInfo)
        plaintext = plaintext.encode('utf-8')
    elif not isinstance(plaintext, bytes):
        loggingError = '[ ' + getCurrentTime() + ' ] Input of invalid type and it can not be hashed'
        logging.error(loggingError)
        raise ValueError('Your input is of invalid type and it can not be hashed')

    try:
        yield Proceed(classInstance, plaintext)
    except Exception as exception:
        print(
            'An error has occurred when you tried to compute your hash, for more information please check your errors log file')
        loggingError = '[ ' + getCurrentTime() + ' ] ' + str(exception)
        logging.error(loggingError)


def getCurrentTime():
    currentTime = datetime.now()
    return currentTime.strftime("%d/%m/%Y %H:%M:%S")
