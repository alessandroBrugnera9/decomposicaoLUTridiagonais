from typing import Tuple
import numpy as np


def buildTestSystem(size: int, cyclic: bool = False) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    aVector = np.zeros(size)
    bVector = np.zeros(size)
    cVector = np.zeros(size)
    dVector = np.zeros(size)

    for n in range(size-1):
        upperValue = (2*(n+1)-1)/(4*(n+1))
        aVector[n] = 1 - upperValue
        bVector[n] = 2
        cVector[n] = upperValue
        dVector[n] = np.cos(2*np.pi*((n+1)**2)/(size**2))
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


def LUDecomposition(aVector, bVector, cVector, L, U):
    # the tridigonalmatrix is represented using only 3 vectors
    n = len(aVector)
    U[0] = bVector[0]
    for i in range(1, n, 1):
        L[i] = aVector[i]/U[i-1]
        U[i] = bVector[i]-L[i]*cVector[i-1]
    return


def resolve_LU_tridiagonal(L, U, d, c, x, y):
    # L,U,d,c,x,y são vetores // este algoritmo supõe uma matriz nxn //
    n = len(L)
    y[0] = d[0]
    for i in range(1, n, 1):
        y[i] = d[i]-L[i]*y[i-1]
    x[n-1] = y[n-1]/U[n-1]
    for j in range(n-2, -1, -1):
        x[j] = (y[j]-c[j]*x[j+1])/U[j]
    return


def main():
    # TODO: define condition for verbose
    aVector, bVector, cVector, dVector = buildTestSystem(6)
    print(aVector, bVector, cVector, dVector)


main()
