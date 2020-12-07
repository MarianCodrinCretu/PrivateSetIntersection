from math import log2

from MOP.OPRFInterceptor import checkKey, checkPlaintextForF, checkResultValidity
from PRF.AESPrfCreator import AESPrfCreator
from PRF.DESPrfCreator import DESPrfCreator
from PRF.PrfScopeEnum import PrfScopeEnum
from Utils.DataUtil import convertBytesIntoBits, splitTextIntoHalves, convertBinaryToDecimal, splitIntoNBlocks, xorStrings
import os


@checkKey
@checkPlaintextForF
@checkResultValidity
def computeOPrfValue(plaintext, key, l1, w, m, prfType='AES', isKeyAsBitString=False, isPlaintextAsBits=False):
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


def getPrfInstance(prfType, key, scope, iv=b''):
    if prfType == 'DES':
        return DESPrfCreator(iv, key, scope)
    else:
        return AESPrfCreator(iv, key, scope)


def getExtendedKey(t, prfType, key):
    seed = os.urandom(16)
    prg = getPrfInstance(prfType, seed, PrfScopeEnum.PRG)
    extendedKey = []
    for index in range(0, t + 1):
        keyIndex = prg.computePrf(key)
        extendedKey.append(keyIndex)
    return extendedKey


def getFkValueAsString(t, keys, prfType, x0, x1, iv=b''):
    gCipherKey0 = getPrfInstance(prfType, keys[0], PrfScopeEnum.GENERATOR, iv)
    gValKey0X0 = gCipherKey0.computePrf(x0)
    gValKey0X0XorX1AsString = xorStrings(x1, gValKey0X0)
    result = b''
    for index in range(1, t + 1):
        gCipherKeyIndex = getPrfInstance(prfType, keys[index], PrfScopeEnum.GENERATOR, iv)
        gValKeyIndexOfGValKey0X0XorX1 = gCipherKeyIndex.computePrf(gValKey0X0XorX1AsString)
        result += gValKeyIndexOfGValKey0X0XorX1
    return result
