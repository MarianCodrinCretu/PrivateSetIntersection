import random


class OTService:
    def __init__(self, transfer_protocol):
        self.transfer_protocol = transfer_protocol

    def receiverOT(self, A, B, w, m):
        for i in range(w):
            A_column = []
            B_column = []
            for line in range(m):
                A_column.append(A[line][i])
                B_column.append(B[line][i])
            data = {"A": A_column, "B": B_column}
            self.transfer_protocol.send_OT(data)

    def receiver_randomOT(self, A, B, w, m):
        for i in range(w):
            A_column = []
            B_column = []
            for line in range(m):
                A_column.append(A[line][i])
                B_column.append(B[line][i])
            r_i1 = [random.randint(0, 1) for c in range(m)]
            delta_i = [int(bool(r_i1[i]) ^ bool(B_column[i])) for i in range(m)]
            data = {"r_0": A_column, "r_1": r_i1, "delta": delta_i}
            self.transfer_protocol.send_OT(data)

    def senderOT(self, s, w, m):
        C = [[0 for c in range(w)] for l in range(m)]
        for it in range(w):
            data = self.transfer_protocol.receiveOT()
            print(data)
            if s[it] == "0":
                selected = data["A"]
            else:
                selected = data["B"]
            for l in range(m):
                C[l][it] = selected[l]
        return C

    def sender_randomOT(self, s, w, m):
        C = [[0 for c in range(w)] for l in range(m)]
        for it in range(w):
            data = self.transfer_protocol.receiveOT()
            print(data)
            if s[it] == "0":
                selected = data["r_0"]
            else:
                selected = [int(bool(data["r_1"][i]) ^ bool(data["delta"][i])) for i in range(m)]
            for l in range(m):
                C[l][it] = selected[l]
        return C
