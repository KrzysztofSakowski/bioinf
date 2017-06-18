import numpy as np
from functions import g_r
from scipy import optimize


def min_g_r(Y, weights, N, q, field_lambda, coupling_lambda, gap_lambda, r, M, nrGapParam, lH, rH, options):
    r = int(r)

    funObj = lambda wr: g_r(wr, Y, weights, N, q, field_lambda, coupling_lambda, gap_lambda, r, M, lH, rH)

    wr0 = np.zeros((q + q ** 2 * (N-1)+nrGapParam, 1))

    #wr = minFunc(funObj,wr0,options);

    optimized_result = optimize.minimize(funObj, wr0, method='BFGS')  # TODO add options

    return -1  # TODO return array from optimized_result
