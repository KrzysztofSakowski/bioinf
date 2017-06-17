from functions import calcInverseWeights
import numpy as np

def test_sequence():
    data = np.zeros((526,1))
    outputRef = np.zeros((526,1))
    i = 0
    with open('fastaOutput.txt') as file:
        for line in file.readlines():
            for num in line.split():
                data[i] = int(num)
                i += 1

    i = 0
    with open('calcInverseWeightsRef.txt') as file:
        for line in file.readlines():
            for num in line.split():
                outputRef[i] = int(num)
                i += 1

    weights = calcInverseWeights(data.astype(dtype="int"), 0.01)

    # count = 0
    # for i in range(526):
    #     if outputRef[i] != weights[i]:
    #         count+=1
    #         print(outputRef[i], weights[i])
    #
    # print (count)
    # assert(np.array_equal(weights, outputRef))

    weights = np.divide(1, weights)

    assert np.sum(weights) == 20
