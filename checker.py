import time
from main import LUDecomposition, solveLUSystem, buildTridiagonalMatrix, buildTestSystem
import numpy as np




def run():
    tic = time.perf_counter()
    # print("Cyclic: ", cyclic)
    aVector, bVector, cVector, dVector = buildTestSystem(matrixSize)

    # creating vectors necessaries to solve cyclic systems
    # building v vector  for cyclic systems
    vVector = np.zeros(matrixSize-1)
    vVector[0] = aVector[0]
    vVector[-1] = cVector[-2]
    # building w vector  for cyclic systems
    wVector = np.zeros(matrixSize-1)
    wVector[0] = cVector[-1]
    wVector[-1] = aVector[-1]

    # Creating n-1xn-1 system from the main Matrix, and solving to find important relations
    LVector, UVector = LUDecomposition(
        aVector[:-1], bVector[:-1], cVector[:-1])
    yTilde = solveLUSystem(LVector, UVector, cVector[:-1], dVector[:-1])
    zTilde = solveLUSystem(LVector, UVector, cVector[:-1], vVector)

    xN = (dVector[-1]-cVector[-1]*yTilde[0]-aVector[-1]*yTilde[-1]) / \
        (bVector[-1]-cVector[-1]*zTilde[0]-aVector[-1]*zTilde[-1])
    xTilde = yTilde-xN*zTilde

    # TODO: Append xVector properly
    xVector = np.append(xTilde, xN)

    aMatrix = buildTridiagonalMatrix(aVector, bVector, cVector)


    # print("Solution: ")
    # print(xVector.tolist())
    # print()
    # # Analyzing the solutions
    # calculatedValue = aMatrix@xVector
    # print("Comparing true value of the system multiplication (D Vector) to A*x:")
    # print((calculatedValue-dVector).tolist())
    # print()
    # print("Residual Quadratic Error: ", np.square(calculatedValue-dVector).sum())
    # print("Mean Root Quadratic Error: ", np.sqrt(
    #     np.square(calculatedValue-dVector).mean()))


    # xSolver = np.linalg.solve(aMatrix, dVector)
    # calculatedValue = aMatrix@xSolver
    # print("Mean Root Quadratic Error Linalg: ", np.sqrt(
    #     np.square(calculatedValue-dVector).mean()))
    # print("Comparing linalg x to calculated: ")
    # print((xSolver-xVector).tolist())
    # print()


    toc = time.perf_counter()
    return (toc - tic)

cyclic = True
matrixSize = 50000

timeArray = []
i=0
while i<10:
    timeArray.append(run())
    i=i+1

print(np.array(timeArray).mean())