
#extract eq
def left(e):
    return e[0]
def op(e):
    return e[1]
def right(e):
    return e[2]

def isInside(v, e):
    if type(e) != type("a"):
        return isInside(v,left(e)) or isInside(v, right(e))
    else:
        return v == e
    
def solve(v, q):
    if isInside(v, left(q)):
        return solving(v,q)
    elif isInside(v, right(q)):
        return solving(v, (right(q), "=", left(q)))
    else:
        return None

def solving(v, e):
    L = left(e)
    if v == L:
        return e
    else:
        return solvingAdd(v,e)

def solvingAdd(v,e):
    A = left(left(e))
    B = right(left(e))
    C = right(e)
    if isInside(v,A):
        return solving (v, (A, "=", (C, "-", B)))
    else:
        return solving(v, (B, "=", (C, "-", A)))
    
