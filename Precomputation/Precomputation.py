import random
from PrecomputationMonitors import check_input_validity, check_update_validity


class Precomputation:

    def __init__(self, dictParameters, dictFunctions, key):
        self.dictParameters = dictParameters
        self.dictFunctions = dictFunctions
        self.key = key

    def computeHash1(self, x):
        return self.dictFunctions[self.dictParameters['hash1']](x)

    def computePRF(self, x, key):
        return self.dictFunctions['FK'](x, key, self.dictParameters['l1'],
                                        self.dictParameters['w'],
                                        self.dictParameters['m'],
                                        self.dictParameters['prf'])

    def compute_v(self, w):

        v = self.computePRF(self.computeHash1(w), self.key)

        return v

    @check_input_validity
    def compute_input(self, input_y):

        result = []

        for i in range(0, len(input_y)):
            result.append(self.compute_v(input_y[i]))

        return result

    @check_update_validity
    def update_d(self, v_list, matrix):

        for i in range(0, len(v_list)):
            matrix[i][v_list[i]] = 0

        return matrix
