from Entity import Entity, Mapper
# from Receiver import Receiver
from aspectlib.test import record
from Transfer import Transfer_Protocol
from Utils import RandomUtils, PSIAlgoUtils


class Sender(Entity):

    @record
    def __init__(self, transfer_protocol):
        # if Receiver.__init__.calls:
        #     if Receiver.__init__.calls[0][1] != self.__init__.calls[0][1]:
        #         raise Exception("Sender and Receiver should have same Transfer_Protocol")
        super().__init__(transfer_protocol)
        mapper = Mapper("Sender")

    def OT(self, transfer_protocol, s):
        C = [[0 for c in range(self.w)] for l in range(self.m)]
        for it in range(self.w):
            data = transfer_protocol.receiveOT()
            print(data)
            if s[it] == "0":
                selected = data["A"]
            else:
                selected = data["B"]
            for l in range(self.m):
                C[l][it] = selected[l]
        return C

    def execute_protocol(self, ip: str, port: str, mapper, transfer_protocol):
        s = RandomUtils.generateSSender(self.w)
        print("s: ", s)
        C = self.OT(transfer_protocol, s)
        print(C)

    def get_data(self):
        print("Sender: get data")

    def end_entity(self):
        self.__init__.calls.clear()


if __name__ == "__main__":
    send = Sender(Transfer_Protocol(""))
    send.execute_protocol("", "", "", send.transfer_protocol)
