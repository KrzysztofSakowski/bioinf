import numpy as np
from functions import g_rC


def g_r(wr, Y, weights, N, q, lambdah, lambdaJ, lambdaG, r, M, lH, rH):

    h_r = np.reshape(wr[1:q], (1, q))
    J_r = np.reshape(wr[q+1:q+q ** 2*(N-1)], (q, q, N-1))
    G = wr[(q+q ** 2*(N-1)+1):]

    r = int(r)

    fval, grad1, grad2, grad3 = g_rC(Y-1, weights, h_r, J_r, [lambdah, lambdaJ, lambdaG], r, G, M, lH, rH)
    grad = [grad1[:], grad2[:], grad3[:]]

    return fval, grad
