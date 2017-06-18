import numpy as np
def min_g_r(Y,weights,N,q,field_lambda,coupling_lambda,gap_lambda,r,M,nrGapParam,lH,rH,options):
    return np.zeros((q + q**2 * (N-1), 1), dtype=np.int32)
