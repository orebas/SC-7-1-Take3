import numpy
import scipy


def pFit(xsubk, fsubk):



    n =len(xsubk)
    vandermonde = numpy.zeros((n,n))
    for i in range(n):
        for k  in range(n):
            vandermonde[i][k] = xsubk[i] ** k
    asubk = numpy.linalg.solve(vandermonde,fsubk)
    return asubk