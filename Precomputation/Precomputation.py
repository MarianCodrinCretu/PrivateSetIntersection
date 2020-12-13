import random
from PrecomputationMonitors import check_input_validity, check_update_validity


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
    def compute_input(self, input_y, key, dictParameters):

        result = []

        for i in range(0, len(input_y)):
            result.append(self.compute_v(input_y[i], key, dictParameters))

        return result

    @check_update_validity
    def update_d(self, v_list, matrix):

        for i in range(0, len(v_list)):
            matrix[i][v_list[i]] = 0

        return matrix
