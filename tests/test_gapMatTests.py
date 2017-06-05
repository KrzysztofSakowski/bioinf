from functions import gapMat
import numpy as np

def test_sequence():
    data = list()
    with open('gapMatData.txt') as file:
        for line in file.readlines():
            for num in line.split():
                data.append(int(num))

    data = np.array(data)
    outputRef = np.empty((500,0))
    lH, rH = gapMat(data.astype(dtype="int"))
    lH = lH.astype(dtype="int")
    rH = rH.astype(dtype="int")
    assert(np.array_equal(lH, outputRef))
    assert(np.array_equal(rH, outputRef))



