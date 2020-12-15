from MOP.PrecomputationMonitors import check_input_validity, check_update_validity


class Precomputation:

    def __init__(self, dictFunctions):
        self.dictFunctions = dictFunctions

    def computeHash1(self, x, dictParameters):
        return self.dictFunctions[dictParameters['hash1']](x)

    def computePRF(self, x, key, dictParameters):
        return self.dictFunctions['FK'](x, key, dictParameters['l1'],
                                        dictParameters['w'],
                                        dictParameters['m'],
                                        dictParameters['prf'])

    def compute_v(self, w, key, dictParameters):

        v = self.computePRF(self.computeHash1(w, dictParameters), key, dictParameters)

        return v

    @check_input_validity
    def compute_v_list(self, input_y, key, dictParameters):

        v_list = []

        for i in range(0, len(input_y)):
            v_list.append(self.compute_v(input_y[i], key, dictParameters))

        return v_list

    @check_update_validity
    def update_d(self, v_list, matrix):

        for i in range(0, len(v_list)):
            for j in range(0, len(v_list[i])):
                matrix[j][v_list[i][j]] = 0

        return matrix
