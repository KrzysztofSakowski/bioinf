from functions import calcInverseWeights
import numpy as np

def test_sequence():
    data = np.zeros((500,1))
    i = 0
    with open('gapMatData.txt') as file:
        for line in file.readlines():
            for num in line.split():
                data[i] = int(num)
                i += 1

    outputRef = np.zeros((500, 1))
    weights = calcInverseWeights(data.astype(dtype="int"), 0.01)
    print(weights)
    # assert(np.array_equal(rH, outputRef))
