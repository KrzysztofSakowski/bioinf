import numpy as np

def g_rC(p_matrix, p_weights, p_h_r, p_J_r, p_lambdas, p_rint, p_G, p_pM, p_lH, p_rH):
    # compute sizes
    nInstances = p_matrix.shape[0]
    nNodes = p_matrix.shape[1]
    nStates = p_h_r.shape[1]
