from functions import gapCount
import numpy as np

def test_sequence():
    data = np.zeros((526,1))
    i = 0
    with open('fastaOutput.txt') as file:
        for line in file.readlines():
            for num in line.split():
                data[i] = int(num)
                i += 1

    outputRef = np.zeros((526, 1))
    lH, rH = gapCount(data.astype(dtype="int"))
    rH = rH.astype(dtype="int")
    assert(np.array_equal(rH, outputRef))
