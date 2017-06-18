import numpy as np
from functions import returnAlignment
from functions import gapMat
from functions import gapCount
from functions import calcInverseWeights
from functions import min_g_r


#TODO Test most outputs against matlab
def gplmDCA_asymmetric(fastafile, outputfile, lambda_h, lambda_J, lambda_G,
                       reweighting_threshold, nr_of_cores, M):

    options = list()
    options.append(['lbfgs', 1e-5, 1e-9, 'off'])

    # Read inputfile (removing inserts), remove duplicate sequences, and calculate weights and B_eff.
    N, B_with_id_seq, q, Y = returnAlignment(fastafile)
    Y = np.vstack({tuple(row) for row in Y})
    lH, rH = gapMat(np.subtract(np.array(Y, dtype=np.int32), 1))
    lH = np.array(lH, dtype=np.int32)
    rH = np.array(rH, dtype=np.int32)
    B, N = Y.shape
    weights = np.ones((B, 1), dtype=np.int32)

    if M > N:
        raise NameError("ERROR: Maximal Gap length must be smaller than length of alignment!")
    if M == -1:
        x, gapHist = gapCount(np.subtract(np.array(Y, dtype=np.int32), 1))
        if np.where(gapHist != 0)[0].size != 0:
            M = np.max(np.where(gapHist != 0)) + 1
            if M > N - 1:
                M = N - 1
        else:
            M = 1

    nrGapParam = np.int32(M * (N - (M + 1) / 2 + 1))

    print("Maximum gap length: ", M)

    if reweighting_threshold > 0.0:
        print("Starting to calculate weights...")
        Y = np.array(Y, dtype=np.int32)
        m = calcInverseWeights(np.subtract(Y, 1), reweighting_threshold)

        weights = np.divide(1, weights)

        print("Finished calculating weights.")

    B_eff = np.sum(weights)

    print("### N = ", N, "B_with_id_seq = ", B_with_id_seq, "B = ", B, "B_eff = ", B_eff, "q = ", q)

    # Prepare inputs to optimizer.
    field_lambda = lambda_h * B_eff
    coupling_lambda = lambda_J * B_eff / 2
    gap_lambda = lambda_G * B_eff / N

    Y = np.array(Y, dtype=np.int32)
    q = np.int32(q)
    w = np.zeros((q + q ** 2 * (N - 1) + nrGapParam, N), dtype=np.int32)

    if nr_of_cores > 1:
        #TODO Add threading
        # nothing yet
        return -1
    else:
        for r in range(N):
            # print("Minimizing g_r for node r=", r)
            wr = min_g_r(Y, weights, N, q, field_lambda, coupling_lambda, gap_lambda, r, M, \
                         nrGapParam, lH, rH, options)
            w[:][r] = wr

    # Extract the coupling estimates from w.
    JJ = np.reshape(w[q: q + q ** 2 * (N - 1)][:], (q, q, N - 1, N))
    Jtemp1 = np.zeros((q, q, N * (N - 1) // 2), dtype=np.int32)
    Jtemp2 = np.zeros((q, q, N * (N - 1) // 2), dtype=np.int32)
    l = 0

    for i in range(N):
        for j in range(i + 1, N + 1, 1):
            #TODO Fix assigning
            # Jtemp1[:][:][l] = JJ[:][:][j - 1][i]  # J_ij as estimated from g_i
            # Jtemp2[:][:][l] = np.transpose(JJ[:][:][i][j])  # J_ij as estimated from g_j
            l += 1

    G = w[q + q ** 2 * (N - 1):, :]

    #TODO Needs previous values
    #Shift the coupling estimates into the Ising gauge.
    J1 = np.zeros((q, q, N * (N - 1) // 2), dtype=np.int32)
    J2 = np.zeros((q, q, N * (N - 1) // 2), dtype=np.int32)

    for l in range((N * (N - 1) // 2)):
        J1[:, :, l] = np.add(np.subtract(np.subtract(
            Jtemp1[:, :, l]
            , np.matlib.repmat(np.mean(Jtemp1[:, :, l]), q, 1))
            , np.matlib.repmat(np.mean(Jtemp1[:, :, l], axis=1), 1, q))
            , np.mean(np.mean(Jtemp1[:, :, l])))

        J2[:, :, l] = np.add(np.subtract(np.subtract(
            Jtemp2[:, :, l]
            , np.matlib.repmat(np.mean(Jtemp2[:, :, l]), q, 1))
            , np.matlib.repmat(np.mean(Jtemp2[:, :, l], axis=1), 1, q))
            , np.mean(np.mean(Jtemp2[:, :, l])))

    # Take J_ij as the average of the estimates from g_i and g_j.
    J = np.multiply(np.add(J1, J2), 0.5)

    #TODO Needs J
    #Calculate frob. norms FN_ij.
    NORMS = np.zeros(N, N)
    l = 1
    for i in range(N-1):
        for j in range(i+1, N):
            NORMS[i][j] = np.linalg.norm(J[:][:][l], 'fro')  # TODO
            NORMS[j][i] = NORMS[j][i]
            l += 1

    #Calculate final scores, CN_ij=FN_ij-(FN_i-)(FN_-j)/(FN_--), where '-'
    #denotes average.

    norm_means = np.division(np.multiply(np.mean(NORMS), N), N-1)
    norm_means_all = np.division(np.multiply(np.mean(np.mean(NORMS)), N), N-1)

    CORRNORMS = np.subtract(NORMS, np.division(np.multiply(np.transpose(norm_means), norm_means), norm_means_all))

    output = []
    for i in range(N-1):
        for j in range(i + 1, N):
            output.append((i, j, CORRNORMS[i][j]))  # TODO is this ok?

    # TODO print out
