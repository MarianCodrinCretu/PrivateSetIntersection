from Crypto.Util.Padding import pad
from aspectlib import Aspect, Proceed, Return


@Aspect
def checkBytesType(inputToCheck):
    if isinstance(inputToCheck, str):
        inputToCheck = inputToCheck.encode("utf-8")
        yield Proceed(inputToCheck)
    elif isinstance(inputToCheck, bytes):
        yield Proceed
    else:
        raise ValueError('Please provide a valid input type')


@Aspect
def checkSplitFunctionValidity(inputToCheck):
    if len(inputToCheck) % 8 != 0:
        raise ValueError('The bytes has not been padded in order to do the splitting correctly')
    result = yield Proceed
    if len(result) != 2 or len(result[0]) != len(result[1]):
        raise Exception('The two halves has not been computed correctly')


@Aspect
def checkBitOperands(operand1, operand2):
    if len(operand1) == len(operand2):
        yield Proceed
    elif len(operand1) > len(operand2):
        operand2 = pad(operand2, len(operand1))
    else:
        operand1 = pad(operand1, len(operand2))
    yield Proceed(operand1, operand2)
