from aspectlib import Aspect, Proceed
import logging
logging.basicConfig(filename='log.csv', level=logging.DEBUG)


@Aspect(bind=True)
def logMatricesBitsErrors(cutpoint, *args):
    D = args[0]
    if len(args) == 2:
        A = args[1]
    else:
        A = None

    for l in range(len(D)):
        for c in range(len(D[l])):
            if D[l][c] not in [0, 1]:
                logging.error(cutpoint.__name__ + ": Matrix D should contain just bits. D[" + str(l) + "][" + str(c) + "] = " + str(D[l][c]))
                raise TypeError("Matrix D should contain just bits")

    if A is not None:
        for l in range(len(A)):
            for c in range(len(A[l])):
                if A[l][c] not in [0, 1]:
                    logging.error(cutpoint.__name__ + ": Matrix A should contain just bits. A[" + str(l) + "][" + str(c) + "] = " + str(A[l][c]))
                    raise TypeError("Matrix A should contain just bits")
    try:
        yield
    except Exception as exception:
        print('Error at computeBReceiver')
        logging.error(cutpoint.__name__ + ": " + str(exception))


@Aspect(bind=True)
def logNotReturnedBitsErrors(cutpoint, *args):
    result = None
    try:
        result = yield
    except Exception as exception:
        print('Error at computeBReceiver')
        logging.error(cutpoint.__name__ + ": " + str(exception))

    if result and (cutpoint.__name__ == "generateSSender" or cutpoint.__name__ == "generateKey"):
        for b in result:
            if b not in ["1", "0"]:
                logging.error(cutpoint.__name__ + " function should return just bits; result contains " + b)
                raise TypeError("Function should return just bits")
    elif result:
        for l in range(len(result)):
            for c in range(len(result[l])):
                if cutpoint.__name__ == "initMatrixDReceiver":
                    if result[l][c] != 1:
                        logging.error(cutpoint.__name__ + " function should return a matrix just with 1s; D[" + str(l) +
                                      "][" + str(c) + "] = " + str(result[l][c]))
                        raise TypeError("Matrix D should contain just 1s")
                elif cutpoint.__name__ == "initMatrixAReceiver":
                    if result[l][c] not in [0, 1]:
                        logging.error(cutpoint.__name__ + " function should return a matrix just with bits; A[" + str(l) +
                                      "][" + str(c) + "] = " + str(result[l][c]))
                        raise TypeError("Matrix A should contain just bits")
