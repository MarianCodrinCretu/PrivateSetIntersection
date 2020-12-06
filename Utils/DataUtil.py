from MOP.DataUtilInterceptor import checkBytesType, checkSplitFunctionValidity, checkByteOperands


def splitIntoBlocks(data, blockSize):
    return [data[blockIndex:blockIndex + blockSize] for blockIndex in range(0, len(data), blockSize)]


def splitIntoNBlocks(data, blocksNumber):
    blockSize = (len(data) + blocksNumber - 1) // blocksNumber

    return [data[blockIndex:blockIndex + blockSize] for blockIndex in range(0, blocksNumber * blockSize, blockSize)]


@checkBytesType
def convertBytesIntoBits(bytesString):
    bytesLength = len(bytesString)
    if bytesLength == 1:
        return '{0:08b}'.format(bytesString)
    elif bytesLength > 1:
        bits = ''
        for index in range(0, bytesLength):
            byteAsBits = '{0:08b}'.format(bytesString[index])
            bits += byteAsBits
        return bits


@checkSplitFunctionValidity
def splitTextIntoHalves(text):
    if len(text) % 2 == 1:
        raise ValueError('The value which needs to be split has to be of even length')
    return [text[0:len(text) // 2], text[len(text) // 2:]]


@checkByteOperands
def computeByteXor(operand1, operand2):
    result = ''
    for index in range(0, len(operand1)):
        result += str(xorBits(operand1[index], operand2[index]))
    return result.encode('utf-8')


def xorBits(bit1, bit2):
    return (int(bit1) + int(bit2)) % 2


def xorStrings(string1, string2):
    return bytes(x ^ y for x, y in zip(string1, string2))


def convertBinaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    for index in reversed(range(0, len(binary))):
        dec = int(binary[index])
        decimal = decimal + dec * pow(2, i)
        i += 1
    return decimal


def convertBitsIntoString(binaryInput):
    stringValue = ''
    for i in range(0, len(binaryInput), 8):
        temporary = int(binaryInput[i:i + 8])
        decimal = int(str(temporary), 2)
        stringValue = stringValue + chr(decimal)
    return stringValue
