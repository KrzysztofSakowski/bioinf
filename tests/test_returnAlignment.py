from functions import returnAlignment
import numpy as np

def test_sequence():
    outputRef = np.zeros((526, 1))  # TODO shape of Y is (4, 526)
    i = 0
    with open('fastaOutput.txt') as file:
        for line in file.readlines():
            for num in line.split():
                outputRef[i] = int(num)
                i += 1

    outputRef = np.add(outputRef, 1)

    N, B, q, Y = returnAlignment("fasta.fas")

    N_ref = 526
    B_ref = 4
    q_ref = 21

    assert N == N_ref
    assert B == B_ref
    assert q == q_ref
    assert np.array_equal(Y, outputRef)  # TODO fails, shapes differ
