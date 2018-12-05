

def pEval(x, asubk):
    x = x * 1.0
    f = asubk[-1] * 1.0
    k = len(asubk) - 2
    while (k >= 0):
        f = f * x + asubk[k] * 1.0
        k = k - 1
    return f
