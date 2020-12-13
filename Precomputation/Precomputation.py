import random
from PrecomputationMonitors import check_input_validity, check_update_validity


class Precomputation:
    __instance = None

    def compute_v(self, w):

        v = [i for i in range(0, w)]
        random.shuffle(v)

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
