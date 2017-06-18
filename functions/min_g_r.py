import numpy as np
from functions.g_r import g_r
from scipy import optimize


def min_g_r(Y, weights, N, q, field_lambda, coupling_lambda, gap_lambda, r, M, nrGapParam, lH, rH, options):
    r = int(r)

    funObj = lambda wr: g_r(wr, Y, weights, N, q, field_lambda, coupling_lambda, gap_lambda, r, M, lH, rH)[0]

    wr0 = np.zeros((q + q ** 2 * (N-1)+nrGapParam, 1))

    options_dict = {
        'disp': None,
        'maxls': 20,
        'iprint': -1,
        'gtol': 1e-05,
        'eps': 1e-08,
        'maxiter': 15000,
        'ftol': 2.220446049250313e-09,
        'maxcor': 10,
        'maxfun': 15000
    }

    optimized_result = optimize.minimize(funObj, wr0, method='L-BFGS-B', options=options_dict)

    return optimized_result.x