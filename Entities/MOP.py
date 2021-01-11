import Entity
from aspectlib import Aspect, Proceed
import logging
import importlib
logging.basicConfig(filename='log.csv', level=logging.DEBUG)


@Aspect(bind=True)
def sameTransferProtocol(cutpoint, *args):
    transferProtocol = args[1]
    instance = args[0]
    if len(Entity.Entity.__init__.calls) > 1:
        transferProtocolUsed = Entity.Entity.__init__.calls[0][1][0]
        if transferProtocol != transferProtocolUsed:
            logging.error(cutpoint.__name__ + "Entities should have same Transfer_Protocol")
        transferProtocol = transferProtocolUsed
    try:
        yield Proceed(instance, transferProtocol)
    except Exception as exception:
        logging.error(cutpoint.__name__ + str(exception))

