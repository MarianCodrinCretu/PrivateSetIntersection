import random
from PrecomputationMonitors import check_input_validity, check_update_validity


def compute_v(w):

    v = [i for i in range(0, w)]
    random.shuffle(v)

    return v


@check_input_validity
def compute_input(input_y):

    result = []

    for i in range(0, len(input_y)):
        result.append(compute_v(input_y[i]))

    return result


@check_update_validity
def update_d(v_list, matrix):

    for i in range(0, len(v_list)):
        matrix[i][v_list[i]] = 0

    return matrix


def xor_b(matrix_a, matrix_d):

    matrix_b = []

    for i in range(0, len(matrix_a)):
        matrix_b.append([])
        for j in range(0, len(matrix_a[i])):
            matrix_b[-1].append(int(matrix_a[i][j] != matrix_d[i][j]))

    return matrix_b
