from Crypto.Util.Padding import pad
from aspectlib import Aspect, Proceed, Return


@Aspect
def addPaddingToTheOutput(classInstance, plaintext):
    yield Proceed
    actualByteLength = len(classInstance._result)
    desiredByteLength = classInstance._desiredOutputByteLength

    if actualByteLength == desiredByteLength:
        pass
        #print('The hash output is already of length', str(classInstance._desiredOutputByteLength))

    elif actualByteLength < desiredByteLength:
        print('The output of hash has been padded')
        classInstance._result = pad(classInstance._result, desiredByteLength)
    else:
        print('The output of hash cannot be padded')
        classInstance._result = None

