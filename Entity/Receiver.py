from Entity import Entity
from aspectlib.test import record


class Receiver(Entity):

    @record
    def __init__(self):
        super().__init__()

    def execute_protocol(self, ip: str, port: str, mapper, transfer_protocol):
        pass

    def get_data(self):
        print("Receiver: get data")

    def start_protocol(self):
        pass

    def setParameters(self, lambda_, sigma, m, w, l1, l2, hash1, hash2, prf, otVariant, data):
         self.dictParameters = {
            'lambda': lambda_,
            'sigma': sigma,
            'm': m,
            'w': w,
            'l1': l1,
            'l2': l2,
            'hash1': hash1,
            'hash2': hash2,
            'prf': prf,
            'otVariant': otVariant,
            'lenDataset': len(data)
         }

    def negociate_parameters(self):
        pass

    def end_entity(self):
        self.__init__.calls.clear()


if __name__ == "__main__":
    recv = Receiver()
