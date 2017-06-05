import numpy as np


def gapCount(p_matrix):
    N = p_matrix.shape[0]
    if len(p_matrix.shape) > 1:
        M = p_matrix.shape[1]
    else:
        M = 0
    gapStretches = np.zeros((N, N), dtype=np.float)
    gapStretchesHist = np.zeros((N, 1), dtype=np.float)

    for i in range(N):
        for j in range(N):
            gapStretches[j][i] = 0

    for m in range(M):
        k = 0
        for i in range (N):
            for j in range(i, N):
                if (p_matrix[j][m]==0):
                    gapStretches[j-i][i] += 1
                else:
                    break

            if p_matrix[i][m] == 0:
                k += 1
            else:
                if (k > 0):
                    gapStretchesHist[k-1] += 1
                    k = 0

    return gapStretches, gapStretchesHist