from math import log2

from MOP.OPRFInterceptor import checkKey, checkPlaintextForF, checkResultValidity
from PRF import PRFCreator
from PRF.PRFCreator import PRFCreator
from Shared.Enums.PrfScopeEnum import PrfScopeEnum
from Shared.Enums.PrfTypeEnum import PrfTypeEnum
from Utils.DataUtil import convertBytesIntoBits, splitTextIntoHalves, convertBinaryToDecimal, splitIntoNBlocks, xorStrings
import os


@checkKey
@checkPlaintextForF
@checkResultValidity
def computeOPrfValue(plaintext, key, l1, w, m, prfType=PrfTypeEnum.AES, isKeyAsBitString=False, isPlaintextAsBits=False):
    plaintextSplitIntoHalves = splitTextIntoHalves(plaintext)

    lambdaValue = int(l1 // 2)

    t = int(w * log2(m) // lambdaValue)

    extendedKeyAsArray = getExtendedKey(t, prfType, key)
    FkValueAsString = getFkValueAsString(t, extendedKeyAsArray, prfType, plaintextSplitIntoHalves[0],
                                         plaintextSplitIntoHalves[1])
    FkValueAsBits = convertBytesIntoBits(FkValueAsString)
    FkValueAsBitArray = splitIntoNBlocks(FkValueAsBits, w)
    return getVAsAWLengthVector(FkValueAsBitArray)


def getVAsAWLengthVector(FkValueAsBitArray):
    return [convertBinaryToDecimal(FkValueAsBitArray[index]) for index in range(0, len(FkValueAsBitArray))]


def getExtendedKey(t, prfType, key):
    #seed = os.urandom(len(key))
    seed = key.encode('utf8')
    prg = PRFCreator(prfType, seed)
    extendedKey = []
    for index in range(0, t + 1):
        keyIndex = prg.computePrf(key, PrfScopeEnum.PRG)
        extendedKey.append(keyIndex)
    return extendedKey


def getFkValueAsString(t, keys, prfType, x0, x1, iv=b''):
    gCipherKey0 = PRFCreator(prfType, keys[0], iv)
    gValKey0X0 = gCipherKey0.computePrf(x0, PrfScopeEnum.GENERATOR)
    gValKey0X0XorX1AsString = xorStrings(x1, gValKey0X0)
    result = b''
    for index in range(1, t + 1):
        gCipherKeyIndex = PRFCreator(prfType, keys[index], iv)
        gValKeyIndexOfGValKey0X0XorX1 = gCipherKeyIndex.computePrf(gValKey0X0XorX1AsString, PrfScopeEnum.GENERATOR)
        result += gValKeyIndexOfGValKey0X0XorX1
    return result
