from NegotiationParameters.NegotiateParameters import NegociateParameters
from NegotiationParameters.NegotiateParametersUtils import NegotiateParametersUtils
import NegotiationParameters.Constants

dictParameters = {
    'lambda': 128,
    'sigma': 60,
    'm': 1,
    'w': 100,
    'l1': 1284,
    'l2': 50,
    'hash1': 'BLAKE2B_32',
    'hash2': 'BLAKE2B_32',
    'prf': 'AES',
    'otVariant': '1',
    'lenDataset': 5
}

negot = NegotiateParametersUtils()
negot2 = NegociateParameters(None, negot)

print(dictParameters)
print('final dict'+ str(negot2.validateParameters(dictParameters)))