from Entity import Entity
from aspectlib.test import record


class Sender(Entity):

    @record
    def __init__(self):
        super().__init__()

    def execute_protocol(self, ip: str, port: str, mapper, transfer_protocol):
        pass

    def get_data(self):
        print("Sender: get data")

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

    def end_entity(self):
        self.__init__.calls.clear()


if __name__ == "__main__":
    send = Sender()
    send.setParameters(128, 60, 1, 100, 256, 50, 'MD5', 'SHA256', 'AES', '1', ['1', '2', '3'])
    print(send.dictParameters)
    # Entity.__init__.calls.clear()
