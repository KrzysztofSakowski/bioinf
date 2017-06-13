import numpy as np

def calcInverseWeights(p_matrix, p_threshold):
    nInstances = p_matrix.shape[0]
    if len(p_matrix.shape) > 1:
        nNodes = p_matrix.shape[1]
    else:
        M = 1

    output = np.zeros((nInstances, 1), dtype=np.float)

    for i in range(nInstances):
        output[i] += 1
        for j in range(i+1,nInstances,1):
            id = 0
            for n in range(nNodes):
                if (p_matrix[i][n] == p_matrix[j][n]):
                    id += 1
            if id >= (1-p_threshold)*nNodes:
                output[i][0]+=1
                output[j][0]+=1


    return output
