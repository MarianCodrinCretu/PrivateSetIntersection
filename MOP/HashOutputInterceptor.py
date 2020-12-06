from Crypto.Util.Padding import pad
from aspectlib import Aspect, Proceed


@Aspect
def addPaddingToTheOutput(classInstance, plaintext):
    yield Proceed
    actualResultBitLength = len(classInstance._result) * 8
    desiredByteLength = int(classInstance._outputBitLength / 8)

    if actualResultBitLength == classInstance._outputBitLength:
        print('The hash output is already of length', str(classInstance._outputBitLength))
        return

    elif actualResultBitLength < classInstance._outputBitLength:
        paddedResult = pad(classInstance._result, desiredByteLength)

    print('The output of hash has been padded')
    classInstance._result = paddedResult


