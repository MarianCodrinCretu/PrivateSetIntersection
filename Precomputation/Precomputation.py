from Precomputation.MOP.PrecomputationMonitors import check_input_validity, check_update_validity


class Precomputation:

    def computeHash1(self, x, functionHash1):
        return functionHash1(x)

    def computePRF(self, x, key, dictParameters, functionPRF):
        return functionPRF(x, key, dictParameters['l1'],
                                        dictParameters['w'],
                                        dictParameters['m'],
                                        dictParameters['prf'])

    def compute_v(self, x, key, dictParameters, functionHash1, functionPRF):

        v = self.computePRF(self.computeHash1(x, functionHash1), key, dictParameters, functionPRF)

        return v

    @check_input_validity
    def compute_v_list(self, input_y, key, dictParameters, functionHash1, functionPRF):

        v_list = []

        for i in range(0, len(input_y)):
            v_list.append(self.compute_v(input_y[i], key, dictParameters, functionHash1, functionPRF))

        return v_list

    @check_update_validity
    def update_d(self, v_list, matrix):

        for i in range(0, len(v_list)):
            for j in range(0, len(v_list[i])):
                matrix[v_list[i][j]][j] = 0

        return matrix
