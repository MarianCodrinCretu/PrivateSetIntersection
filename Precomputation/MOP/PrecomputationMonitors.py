from aspectlib import Aspect, Proceed
from datetime import datetime
import logging
logging.basicConfig(filename='../logs.log', level=logging.DEBUG)


def get_current_time():
    current_time = datetime.now()
    return current_time.strftime("%d/%m/%Y %H:%M:%S")


@Aspect
def check_input_validity(*args):
    v_array = args[1]

    if v_array != [i for i in v_array if i.isascii() and i.isprintable()]:

        logging_error = '[ ' + get_current_time() + ' ] Input of invalid type and it can not be used to compute V'
        logging.error(logging_error)
        raise ValueError('The input is of invalid type and it can not be used to compute V')

    try:
        yield Proceed(*args)
    except Exception as exception:
        print(
            'An error has occurred during input computation, for more information please check your errors log file')
        logging_error = '[ ' + get_current_time() + ' ] ' + str(exception)
        logging.error(logging_error)


@Aspect
def check_update_validity(*args):
    matrix = args[2]

    # Matrix check

    if len([j for i in range(0, len(matrix)) for j in range(0, len(matrix[i]))
            if isinstance(matrix[i][j], bool) or str(matrix[i][j]).isnumeric()]) == len(matrix)*len(matrix[0]):

        logging_info = '[ ' + get_current_time() + ' ] The string, boolean or int values that were not 0 or 1 were converted to make D valid'
        logging.info(logging_info)

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if isinstance(matrix[i][j], bool) or matrix[i][j] in [0, '0', 1, '1']:
                    matrix[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]) < 0:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = 1

    else:

        logging_error = '[ ' + get_current_time() + ' ] The matrix D contains elements of invalid type'
        logging.error(logging_error)
        raise ValueError('The matrix D contains elements of invalid type')

    try:
        yield Proceed(*args)
    except Exception as exception:
        print(
            'An error has occurred when you tried to update the matrix D, for more information please check your errors log file')
        logging_error = '[ ' + get_current_time() + ' ] ' + str(exception)
        logging.error(logging_error)