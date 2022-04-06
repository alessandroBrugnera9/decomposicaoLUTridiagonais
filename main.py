from typing import Tuple
import numpy as np


def checkTridiagional(matrix: np.ndarray) -> bool:  # TODO: receive np matrix
    size = len(matrix)
    if(size != len(matrix[0])):
        if (verbose):
            print("Non square Matrix")
        return False

    for i in range(size):
        for j in range(size):
            if matrix[i][j] != 0:
                if (i == j):
                    continue
                elif (i-1 == j):
                    continue
                elif (i == j-1):
                    continue
                else:
                    return (False)
    return True


def checkUpperTriangualar(matrix: np.ndarray) -> bool:  # TODO: receive np matrix
    size = len(matrix)
    if(size != len(matrix[0])):
        if (verbose):
            print("Non square Matrix")
        return False

    for i in range(size):
        for j in range(size):
            if matrix[i][j] != 0:
                if (i == j):
                    continue
                elif (i < j):
                    continue
                else:
                    return False
    return True


def checkLowerTriangualar(matrix: np.ndarray) -> bool:  # TODO: receive np matrix
    size = len(matrix)
    if(size != len(matrix[0])):
        if (verbose):
            print("Non square Matrix")
        return False

    for i in range(size):
        for j in range(size):
            if matrix[i][j] != 0:
                if (i == j):
                    continue
                elif (i > j):
                    continue
                else:
                    return False
    return True


def checkLU(lMatrix, uMatrix) -> bool:  # TODO receive 2 matrixes
    if (not checkLowerTriangualar(lMatrix)):
        if (verbose):
            print("L not lower")
        return False

    if (not checkUpperTriangualar(uMatrix)):
        if (verbose):
            print("U not upper")
        return False

    return True


def buildTestSystem(size: int) -> Tuple[np.ndarray, np.ndarray]:
    aMatrix = np.zeros((size, size))
    bMatrix = np.zeros((size, 1))

    for n in range(size-1):
        upperValue = (2*(n+1)-1)/(4*(n+1))
        # main diagonal
        aMatrix[n][n] = 2

        # upper diagonal
        aMatrix[n][n+1] = 1 - upperValue

        # lower diagonal
        aMatrix[n][n-1] = upperValue

        bMatrix[n][0] = np.cos(2*np.pi*(n**2)/(size**2))
    # overriding last entry
    upperValue = (2*size-1)/(4*size)
    aMatrix[size-1][size-1] = 2
    aMatrix[size-1][0] = 1 - upperValue
    aMatrix[size-1][size-1-1] = upperValue

    return aMatrix, bMatrix


verbose = True


def main():
    # TODO: define condition for verbose
    m=buildTestSystem(6)[0]

    
main()
