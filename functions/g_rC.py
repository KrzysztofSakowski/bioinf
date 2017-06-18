import numpy as np


def GindStart(sigma, N):
    return (sigma - 1) * N - (sigma - 1) * ((sigma - 1) + 1) // 2 + sigma - 1


def g_rC(p_matrix, p_weights, p_h_r, p_J_r, p_lambdas, r, p_G, M, p_lH, p_rH):
    # compute sizes
    y = p_matrix

    nNodes = p_matrix.shape[1]
    nStates = p_h_r.shape[0]
    nInstances = p_matrix.shape[0]

    # M = p_pM[0]  # ?

    fM = float(M)
    fnNodes = float(nNodes)
    nrGapParam = int(fM*(fnNodes-(fM+1)//2+1))  # // or / ?

    # allocate memory

    logPot = np.zeros(nStates, dtype=np.double)
    z = np.zeros(1, dtype=np.double)
    nodeBel = np.zeros(nStates, dtype=np.double)

    # output
    fval = np.zeros((1, 1), dtype=np.double)
    fval[0] = 0

    grad1 = np.zeros((nStates, 1), dtype=np.double)
    grad2 = np.zeros((nStates*nStates*(nNodes-1), 1), dtype=np.double)
    grad3 = np.zeros((nrGapParam, 1), dtype=np.double)

    for i in range(0, nrGapParam):
        grad3[0] = 0.0

    # r = p_rint[0] - 1
    r = r - 1

    for i in range(0, nInstances):

        #  Some notes on variable names:
        #  logPot contains, for the current sequence i,
        #  the exponentials in the pseudolikelihood:
        #  logPot(s)=h_r(s)+sum_{j!=r}J_{rj}(s,sigma^(i)_j).
        #  nodeBel is the conditional probability P(sigma_r=s|sigma_{\r}=sigma^(i)_{\r}), i.e.,
        #  nodeBel(s) = e^[ logPot(s) ] / sum_l e^[ logPot(l) ].
        #  z is the denominator of nodeBel.

        for s in range(0, nStates):
            logPot[s] = p_h_r[s]

        for n in range(0, nNodes):
            if n != r:
                y2 = y[i + nInstances*n]
                for s in range(0, nStates):
                    ind = s + nStates*(y2+nStates*(n-(n > r)))
                    logPot[s] = p_J_r[s + nStates*(y2+nStates*(n-(n > r)))]

        # Add GAP parameters
        # Restitute r by a gap
        length = 1
        index = r+1

        if r < nNodes-1:
            length = length + p_rH[i+nInstances*(r+1)]

        if r > 0:
            length = length + p_lH[i+nInstances * (r-1)]
            index = index - p_lH[i+nInstances * (r-1)]

        logPot[0] += p_G[GindStart(length, nNodes)+index-1]

        # Restitute r by non-gap
        # Look if there is now a gap to the right

        if r < nNodes-1:
            if p_rH[i+nInstances*(r+1)] != 0:

                length = p_rH[i+nInstances*(r+1)]
                index = (r+1)+1

                for s in range(1, nStates):
                    logPot[s] += p_G[GindStart(length, nNodes)+index-1]

        # Look if there is a gap to the left

        if r > 0:
            if p_lH[i+nInstances*(r-1)] != 0:

                length = p_lH[i+nInstances*(r-1)]
                index = (r+1)-length

                for s in range(1, nStates):
                    logPot[s] += p_G[GindStart(length, nNodes)+index-1]

        z[0] = 0
        for s in range(0, nStates):
            z[0] += np.exp(logPot[s])  # TODO exp?

        fval[0] -= p_weights[i] * logPot[y[i + nInstances * r]]
        fval[0] += p_weights[i] * np.log(z[0])  # TODO log?

        # Gradient:

        for s in range(0, nStates):
            nodeBel[s] = np.exp(logPot[s] - np.log(z[0]))

        y1 = y[i + nInstances * r]
        grad1[y1] -= p_weights[i] * 1

        for s in range(0, nStates):
            grad1[s] += p_weights[i] * nodeBel[s]

        for n in range(0, nNodes):
            if n != r:
                y2 = y[i + nInstances * n]

                grad2[y1+nStates * (y2+nStates * (n-(n > r)))] -= p_weights[i]

                for s in range(0, nStates):
                    grad2[s+nStates * (y2+nStates * (n-(n > r)))] += p_weights[i] * nodeBel[s]

        # Gap gradient
        # Restitute r by a gap

        length = 1
        index = (r + 1)

        if r < nNodes - 1:
            length = length + p_rH[i + nInstances * (r + 1)]

        if r > 0:
            length = length + p_lH[i+nInstances * (r-1)]
            index = index - p_lH[i+nInstances * (r-1)]

        grad3[GindStart(length, nNodes) + index - 1] += p_weights[i] * nodeBel[0]

        if y[i + nInstances * r] == 0:
            grad3[GindStart(length, nNodes) + index - 1] -= p_weights[i]

        # Restitute r by non-gap
        # Look if there is now a gap to the right

        if r < nNodes-1:
            if p_rH[i+nInstances*(r+1)] != 0:

                length = p_rH[i+nInstances*(r+1)]
                index = (r+1)+1

                for s in range(1, nStates):
                    grad3[GindStart(length, nNodes)+index-1] += p_weights[i] * nodeBel[s]

                if y[i+nInstances*r] != 0:
                    grad3[GindStart(length, nNodes)+index-1] -= p_weights[i]

        # Look if there is a gap to the left

        if r > 0:
            if p_lH[i + nInstances * (r - 1)] != 0:

                length = p_lH[i + nInstances * (r - 1)]
                index = (r + 1) - length

                for s in range(1, nStates):
                    grad3[GindStart(length, nNodes)+index-1] += p_weights[i] * nodeBel[s]

                if y[i+nInstances * r] != 0:
                    grad3[GindStart(length, nNodes)+index-1] -= p_weights[i]

    # Add contributions from R_l2

    for s in range(0, nStates):
        fval[0] += p_lambdas[0] * p_h_r[s] * p_h_r[s]
        grad1[s] += p_lambdas[0] * 2 * p_h_r[s]

    for j in range(0,  nrGapParam):
        fval[0] += p_lambdas[2] * p_G[j] * p_G[j]
        grad3[j] += p_lambdas[2] * 2 * p_G[j]

    for n in range(0, nNodes):
        if n != r:
            for s in range(0, nStates):
                for t in range(0, nStates):

                    fval[0] += p_lambdas[1] * p_J_r[s+nStates * (t+nStates * (n-(n > r)))] * p_J_r[s+nStates * (t+nStates * (n-(n > r)))]
                    grad2[s+nStates * (t+nStates * (n-(n > r)))] += p_lambdas[1] * 2 * p_J_r[s+nStates * (t+nStates * (n-(n > r)))]

    return fval, grad1, grad2, grad3
