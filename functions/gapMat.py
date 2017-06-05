import numpy as np

def gapMat(p_matrix):
    N = p_matrix.shape[0]
    if len(p_matrix.shape) > 1:
        M = p_matrix.shape[1]
    else:
        M = 1
    leftGapMat = np.zeros((N, M), dtype=float)
    rightGapMat = np.zeros((N, M), dtype=float)

    k1 = 0
    k2 = 0
    n2 = 0

    for m in range(M):
        k1 = 0
        k2 = 0
        for n in range(N-1, -1, -1):
            if p_matrix[n][m] == 0:
                k1 += 1
            else:
                k1 = 0
            rightGapMat[n][m] = k1
            n2 = N-n-1
            if p_matrix[n2][m] == 0:
                k2 += 1
            else:
                k2 = 0
            leftGapMat[n2][m] = k2

    return leftGapMat, rightGapMat
