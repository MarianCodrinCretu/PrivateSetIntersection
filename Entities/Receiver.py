from Entity import Entity, Mapper
# from Sender import Sender
from aspectlib.test import record
from Transfer import Transfer_Protocol
from Utils import RandomUtils, PSIAlgoUtils


class Receiver(Entity):

    @record
    def __init__(self, transfer_protocol):
        # if Sender.__init__.calls:
        #     if Sender.__init__.calls[0][1] != self.__init__.calls[0][1]:
        #         raise Exception("Sender and Receiver should have same Transfer_Protocol")
        super().__init__(transfer_protocol)
        mapper = Mapper("Receiver")

    def OT(self, transfer_protocol, A, B):
        for i in range(self.w):
            A_column = []
            B_column = []
            for line in range(self.m):
                A_column.append(A[line][i])
                B_column.append(B[line][i])
            data = {"A": A_column, "B": B_column}
            transfer_protocol.send_OT(data)

    def execute_protocol(self, ip: str, port: str, mapper, transfer_protocol):
        A = RandomUtils.initMatrixAReceiver(self.m, self.w)
        D = RandomUtils.initMatrixAReceiver(self.m, self.w)
        B = PSIAlgoUtils.computeBReceiver(D, A)
        print(A)
        print(B)
        self.OT(transfer_protocol, A, B)

    def get_data(self):
        print("Receiver: get data")

    def start_protocol(self):
        pass

    def negociate_parameters(self):
        pass

    def end_entity(self):
        self.__init__.calls.clear()


if __name__ == "__main__":
    recv = Receiver(Transfer_Protocol(""))
    recv.execute_protocol("", "", "", recv.transfer_protocol)
