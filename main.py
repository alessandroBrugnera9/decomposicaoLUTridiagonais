from typing import Tuple
import numpy as np


def buildTestSystem(size: int, cyclic: bool = False) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    aVector = np.zeros(size)
    bVector = np.zeros(size)
    cVector = np.zeros(size)
    dVector = np.zeros(size)

    for i in range(size-1):
        upperValue = (2*(i+1)-1)/(4*(i+1))
        aVector[i] = 1 - upperValue
        bVector[i] = 2
        cVector[i] = upperValue
        dVector[i] = np.cos(2*np.pi*((i+1)**2)/(size**2))
    # overriding last entry
    upperValue = (2*size-1)/(4*size)
    aVector[size-1] = 1 - upperValue
    bVector[size-1] = 2
    cVector[size-1] = upperValue
    dVector[size-1] = 1

    if(not cyclic):
        aVector[0] = 0
        cVector[-1] = 0

    return (aVector, bVector, cVector, dVector)


verbose = True


def LUDecomposition(aVector, bVector, cVector):
    # the tridigonalmatrix is represented using only 3 vectors
    # only the important value of L (upperdiagonal),U(maindiagional) are calculated
    size = len(aVector)

    LVector = np.zeros(size)
    UVector = np.zeros(size)
    UVector[0] = bVector[0]

    for i in range(1, size):
        L[i] = aVector[i]/U[i-1]
        U[i] = bVector[i]-L[i]*cVector[i-1]
    
    return (LVector,UVector)


def solveLUSystem(LVector, UVector, dVector, cVector):
    # L,U,d,c,x,y are vectors necessay to solve the linear syste
    size = len(LVector)
    xVector = np.zeros(size)
    yVector = np.zeros(size)
    yVector[0] = dVector[0]

    for i in range(1, size):
        yVector[i] = dVector[i]-LVector[i]*yVector[i-1]
    xVector[size-1] = yVector[size-1]/UVector[size-1]
    for j in range(size-2, -1, -1):
        xVector[j] = (yVector[j]-cVector[j]*xVector[j+1])/UVector[j]
    
    return (xVector,yVector)


def main():
    # TODO: define condition for verbose
    aVector, bVector, cVector, dVector = buildTestSystem(6)
    print(aVector, bVector, cVector, dVector)


main()
