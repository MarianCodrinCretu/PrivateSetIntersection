"""Definition of meta model 'crypto_ecor'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'crypto_ecor'
nsURI = 'http://cryptoEcore/1.0'
nsPrefix = 'cryptoEcore'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class Entity(EObject, metaclass=MetaEClass):

    lambda_ = EAttribute(eType=EInt, derived=False, changeable=True)
    sigma = EAttribute(eType=EInt, derived=False, changeable=True)
    m = EAttribute(eType=EInt, derived=False, changeable=True)
    w = EAttribute(eType=EInt, derived=False, changeable=True)
    l1 = EAttribute(eType=EInt, derived=False, changeable=True)
    l2 = EAttribute(eType=EInt, derived=False, changeable=True)

    def __init__(self, *, lambda_=None, sigma=None, m=None, w=None, l1=None, l2=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if lambda_ is not None:
            self.lambda_ = lambda_

        if sigma is not None:
            self.sigma = sigma

        if m is not None:
            self.m = m

        if w is not None:
            self.w = w

        if l1 is not None:
            self.l1 = l1

        if l2 is not None:
            self.l2 = l2


class Mapping(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class TransferProtocol(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class AlgoDecoder(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class DataEngineering(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class ClientInterface(EObject, metaclass=MetaEClass):

    receiver = EReference(ordered=True, unique=True, containment=True, upper=-1)
    dataEngineering = EReference(ordered=True, unique=True, containment=True, upper=-1)
    algoDecoder = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, receiver=None, dataEngineering=None, algoDecoder=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if receiver:
            self.receiver.extend(receiver)

        if dataEngineering:
            self.dataEngineering.extend(dataEngineering)

        if algoDecoder:
            self.algoDecoder.extend(algoDecoder)


class ServerInterface(EObject, metaclass=MetaEClass):

    Sender = EReference(ordered=True, unique=True, containment=True, upper=-1)
    dataEngineering = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, Sender=None, dataEngineering=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if Sender:
            self.Sender.extend(Sender)

        if dataEngineering:
            self.dataEngineering.extend(dataEngineering)


class Receiver(Entity):

    ip = EAttribute(eType=EString, derived=False, changeable=True)
    port = EAttribute(eType=EInt, derived=False, changeable=True)
    mapper = EAttribute(eType=Mapping, derived=False, changeable=True)
    transfProt = EAttribute(eType=TransferProtocol, derived=False, changeable=True)
    data = EAttribute(eType=EByteArray, derived=False, changeable=True)

    def __init__(self, *, ip=None, port=None, mapper=None, transfProt=None, data=None, **kwargs):

        super().__init__(**kwargs)

        if ip is not None:
            self.ip = ip

        if port is not None:
            self.port = port

        if mapper is not None:
            self.mapper = mapper

        if transfProt is not None:
            self.transfProt = transfProt

        if data is not None:
            self.data = data


class Sender(Entity):

    ip = EAttribute(eType=EString, derived=False, changeable=True)
    port = EAttribute(eType=EInt, derived=False, changeable=True)
    mapper = EAttribute(eType=Mapping, derived=False, changeable=True)
    transfProt = EAttribute(eType=TransferProtocol, derived=False, changeable=True)
    data = EAttribute(eType=EByteArray, derived=False, changeable=True)

    def __init__(self, *, ip=None, port=None, mapper=None, transfProt=None, data=None, **kwargs):

        super().__init__(**kwargs)

        if ip is not None:
            self.ip = ip

        if port is not None:
            self.port = port

        if mapper is not None:
            self.mapper = mapper

        if transfProt is not None:
            self.transfProt = transfProt

        if data is not None:
            self.data = data
