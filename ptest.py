import peval
import pfit
import random
import numpy as np

if __name__== "__main__":

    #test Horner's method implementation vs Pythons
    maxabserr = 0
    maxpolyval=0
    for i in range(10):
        d =    random.randint(2,20)
        xs = [0]*(d+1)
        for j in range(d+1):
            xs[j] = random.random() * 5 - 10
        #print(xs)
        for j in range(-10,10):
            t1 = peval.pEval(j * 1.0,xs)
            ys = np.flipud(xs)
            t2 = np.polyval(ys,j * 1.0)
            maxmabserr = max(maxabserr, abs(t1-t2))
            maxpolyval = max(maxpolyval,t1)
    print (maxabserr)
    print (maxpolyval)



    xsubk = (0,2.5,3.14,-3,-2)
    fsubk = (-2,5.5,10,-2,-5)
    #asubk = pfit.pFit(xsubk,fsubk)
    #print (asubk)
    #for i in range(len(xsubk)):
    #    print (peval.pEval(xsubk[i],asubk), fsubk[i])
