
from .crypto_ecor import getEClassifier, eClassifiers
from .crypto_ecor import name, nsURI, nsPrefix, eClass
from .crypto_ecor import Entity, Receiver, Sender, AlgoDecoder, DataEngineering, ClientInterface, ServerInterface


from . import crypto_ecor

__all__ = ['Entity', 'Receiver', 'Sender', 'AlgoDecoder',
           'DataEngineering', 'ClientInterface', 'ServerInterface']

eSubpackages = []
eSuperPackage = None
crypto_ecor.eSubpackages = eSubpackages
crypto_ecor.eSuperPackage = eSuperPackage

ClientInterface.receiver.eType = Receiver
ClientInterface.dataEngineering.eType = DataEngineering
ClientInterface.algoDecoder.eType = AlgoDecoder
ServerInterface.Sender.eType = Sender
ServerInterface.dataEngineering.eType = DataEngineering

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
