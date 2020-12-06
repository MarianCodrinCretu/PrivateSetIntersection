from aspectlib import Aspect, Proceed, Return

from Utils.DataUtil import convertBytesIntoBits, convertBitsIntoString


@Aspect
def checkKey(plaintext, key, l1, w, m, prfType='AES', isKeyAsBitString=False, isPlaintextAsBits=False):
    lambdaValue = int(l1 // 2)
    if isKeyAsBitString and len(key) != lambdaValue:
        raise ValueError('Wrong key, please provide another key')

    if len(convertBytesIntoBits(key)) != lambdaValue:
        raise ValueError('Wrong key, please provide another key')

    yield Proceed(plaintext, key, l1, w, m, prfType, isKeyAsBitString, isPlaintextAsBits)


@Aspect
def checkPlaintextForF(plaintext, key, l1, w, m, prfType='AES', isKeyAsBitString=False, isPlaintextAsBits=False):
    if isKeyAsBitString:
        plaintext = convertBitsIntoString(plaintext)
    if len(plaintext) != l1 // 8:
        raise ValueError('Wrong input for F, please provide another input!')

    yield Proceed(plaintext, key, l1, w, m, prfType, isKeyAsBitString, isPlaintextAsBits)


@Aspect
def checkResultValidity(plaintext, key, l1, w, m, prfType='AES', isKeyAsBitString=False, isPlaintextAsBits=False):
    v = yield Proceed
    for index in range(0, len(v)):
        if v[index] > m:
            yield Return
    print('The result has been checked')
    yield Return(v)
