from functions import gapMat
import numpy as np

def test_sequence():
    data = np.zeros((526,1))
    i = 0
    with open('fastaOutput.txt') as file:
        for line in file.readlines():
            for num in line.split():
                data[i] = int(num)
                i += 1

    outputRef = np.zeros((526,1))
    lH, rH = gapMat(data.astype(dtype="int"))
    lH = lH.astype(dtype="int")
    rH = rH.astype(dtype="int")

    assert(np.array_equal(lH, outputRef))
    assert(np.array_equal(rH, outputRef))



