import os
from pyecore.ecore import *
from pyecore.resources import ResourceSet, URI
from pyecoregen.ecore import EcoreGenerator


# Entity class definition
Entity = EClass('Entity')
attribute_list = [EAttribute('lambda', EInt), EAttribute('sigma', EInt), EAttribute('m', EInt),
                  EAttribute('w', EInt), EAttribute('l1', EInt), EAttribute('l2', EInt)]
for i in attribute_list:
    Entity.eStructuralFeatures.append(i)

# Receiver class definition
Receiver = EClass('Receiver', superclass=Entity)
attribute_list = [EAttribute('ip', EString), EAttribute('port', EInt), EAttribute('mapper', EInt),
                  EAttribute('transfProt', EInt), EAttribute('data', EByteArray)]

for i in attribute_list:
    Receiver.eStructuralFeatures.append(i)


# Sender class definition
Sender = EClass('Sender', superclass=Entity)
attribute_list = [EAttribute('ip', EString), EAttribute('port', EInt), EAttribute('mapper', EInt),
                  EAttribute('transfProt', EInt), EAttribute('data', EByteArray)]

for i in attribute_list:
    Sender.eStructuralFeatures.append(i)


# Two empty classes used as reference for the Interface classes.
AlgoDecoder = EClass('AlgoDecoder')
DataEngineering = EClass('DataEngineering')

# ClientInterface class definition and adding references to other classes
ClientInterface = EClass('ClientInterface')
ClientInterface.eStructuralFeatures.append(EReference('receiver', eType=Receiver, upper=-1, containment=True))
ClientInterface.eStructuralFeatures.append(EReference('dataEngineering', eType=DataEngineering, upper=-1, containment=True))
ClientInterface.eStructuralFeatures.append(EReference('algoDecoder', eType=AlgoDecoder, upper=-1, containment=True))


# ServerInterface class definition and adding references to other classes
ServerInterface = EClass('ServerInterface')
ServerInterface.eStructuralFeatures.append(EReference('Sender', eType=Sender, upper=-1, containment=True))
ServerInterface.eStructuralFeatures.append(EReference('dataEngineering', eType=DataEngineering, upper=-1, containment=True))


# Add all the concepts to an EPackage
cwd = os.getcwd()
ecore_schema = EPackage('crypto_ecor', nsURI='http://cryptoEcore/1.0', nsPrefix='cryptoEcore')
ecore_schema.eClassifiers.extend([Entity, Receiver, Sender, AlgoDecoder, DataEngineering, ClientInterface, ServerInterface])

rset = ResourceSet()
resource = rset.create_resource(URI(os.path.join(cwd, 'resource.xmi')))  # This will create an XMI resource
resource.append(ecore_schema)  # we add the EPackage instance in the resource
resource.save()  # we then serialize it


# Generate the python code following the data from the previous EPackage
# A new directory will be created, where a file .py will be created containing the code.
generator = EcoreGenerator()
generator.generate(ecore_schema, cwd)

