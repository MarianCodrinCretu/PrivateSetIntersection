from aspectlib import Aspect, Proceed, Return


@Aspect
def checkKey(plaintext, key, l1, w, m, prfType='AES', isKeyAsBitString=False, isPlaintextAsBits=False):
    lambdaValue = l1 // 2

    if isKeyAsBitString and len(key) != lambdaValue:
        raise ValueError('Wrong key, please provide another key')

    if not isKeyAsBitString and len(key) != lambdaValue // 8:
        raise ValueError('Wrong key, please provide another key')

    yield Proceed(plaintext, key, l1, w, m, prfType, isKeyAsBitString, isPlaintextAsBits)


@Aspect
def checkPlaintextForF(plaintext, key, l1, w, m, prfType='AES', isKeyAsBitString=False, isPlaintextAsBits=False):
    if isPlaintextAsBits and len(plaintext) != l1:
        raise ValueError('Wrong input for F, please provide another input!')

    if not isPlaintextAsBits and len(plaintext) != l1 // 8:
        raise ValueError('Wrong input for F, please provide another input!')

    yield Proceed(plaintext, key, l1, w, m, prfType, isKeyAsBitString, isPlaintextAsBits)


@Aspect
def checkResultValidity(plaintext, key, l1, w, m, prfType='AES', isKeyAsBitString=False, isPlaintextAsBits=False):
    v = yield Proceed

    if len(v) != w:
        print('The result does not have the required length')
        yield Return

    for index in range(0, len(v)):
        if v[index] > m-1:
            print('The result does not have correct values')
            yield Return

    print('The result has been checked')
    yield Return(v)
