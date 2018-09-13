#outca003_lab1.py
#stude122_lab1.py

def left(e):
  return e[0]
def op(e):
  return e[1]
def right(e):
  return e[2]

def isInside(v,e):
  if len(e) > 1:
    if isInside(v,left(e)):
      return True
    elif isInside(v,right(e)):
      return True
    else:
      return False
  elif v==e:
    return True
  else:
    return False

def solve(v,q):
  if isInside(v,left(q)):
    return solving(v,q)
  elif isInside(v,right(q)):
    return solving(v,(right(q),op(q),left(q)))
  else:
    return None


def solving(v,q):
  if v==left(q):
    return q
  elif op(left(q))=='+':
    return solvingAdd(v,q)
  elif op(left(q))=='-':
    return solvingSubtract(v,q)
  elif op(left(q))=='*':
    return solvingMultiply(v,q)
  elif op(left(q))=='/':
    return solvingDivide(v,q)
  else:
    return None

def solvingAdd(v,q):
  if isInside(v,left(left(q))):
    return solving(v,(left(left(q)),op(q),(right(q),'-',right(left(q)))))
  elif isInside(v,right(left(q))):
    return solving(v,(right(left(q)),op(q),(right(q),'-',left(left(q)))))
  else:
    return None

def solvingSubtract(v,q):
  if isInside(v,left(left(q))):
    return solving(v,(left(left(q)),op(q),(right(q),'+',right(left(q)))))
  elif isInside(v,right(left(q))):
    return solving(v,(right(left(q)),op(q),(left(left(q)),'-',right(q))))
  else:
    return None
  
def solvingMultiply(v,q):
  if isInside(v,left(left(q))):
    return solving(v,(left(left(q)),op(q),(right(q),'/',right(left(q)))))
  elif isInside(v,right(left(q))):
    return solving(v,(right(left(q)),op(q),(right(q),'/',left(left(q)))))
  else:
    return None

def solvingDivide(v,q):
  if isInside(v,left(left(q))):
    return solving(v,(left(left(q)),op(q),(right(q),'*',right(left(q)))))
  elif isInside(v,right(left(q))):
    return solving(v,(right(left(q)),op(q),(left(left(q)),'/',right(q))))
  else:
    return None
  