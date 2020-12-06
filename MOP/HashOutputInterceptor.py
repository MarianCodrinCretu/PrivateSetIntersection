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

    # elif actualResultBitLength > classInstance._outputBitLength:
        # blocks = splitIntoBlocks(classInstance._result, desiredByteLength)
        # paddedResult = []
        # for blockIndex in range(0, len(blocks)):
        #     paddedResult.append(pad(blocks[blockIndex], desiredByteLength))
        # raise ValueError('Please provide a valid value')

    print('The output of hash has been padded')
    classInstance._result = paddedResult


