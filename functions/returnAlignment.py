from Bio import SeqIO
import numpy as np
from functions.letter2number import letter2number


def returnAlignment(fastaFile):
    alignFull = list(SeqIO.parse(fastaFile, "fasta"))
    B = sum(1 for x in alignFull)
    arr1 = np.array(alignFull[0].seq)
    arr2 = np.array([char.upper() for char in alignFull[0]])
    ind1 = np.zeros((arr1.shape[0], 1))
    ind2 = np.zeros((arr1.shape[0], 1))
    ind = np.zeros((arr1.shape[0], 1))
    for i in range(arr1.shape[0]):
        if arr1[i] == arr2[i]:
            ind2[i] = True
        else:
            ind2[i] = False
        if arr1[i] == '.':
            ind1[i] = False
        else:
            ind1[i] = True

    for i in range(arr1.shape[0]):
        if ind1[i] == 1 and ind2[i] == 1:
            ind[i] = True
        else:
            ind[i] = False

    N = int(np.sum(ind))

    output = np.zeros((B, N), dtype=np.int)

    for i in range(B):
        counter = -1;
        for j in range(len(ind)):
            if ind[j] == 1:
                counter += 1
                output[i][counter] = letter2number(alignFull[i].seq[j])

    q = np.max(np.max(output))

    return N, B, q, output
