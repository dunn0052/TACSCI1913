# Andrew Hou, collaborated with Joshua Ding

def isInside(variable, expression) :
    if len(expression) == 1 :
        if variable == expression :
           return True
        return False

    if variable == expression[0] or variable == expression[2] :
        return True

    return isInside(variable, expression[0]) or isInside(variable, expression[2])

def solvingAdd(variable, equation) :
    if isInside(variable, equation[0][0]) :
        left = equation[0][0]
        right = (equation[2], '-', equation[0][2])

        return solving(variable,(left, '=', right))

    elif isInside(variable, equation[0][2]) :
        left = equation[0][2]
        right = (equation[2], '-', equation[0][0])
        
        return solving(variable,(left, '=', right))

def solvingSubtract(variable, equation) :
    if isInside(variable, equation[0][0]) :
        left = equation[0][0]
        right = (equation[2], '+', equation[0][2])

        return solving(variable,(left, '=', right))

    elif isInside(variable, equation[0][2]) :
        left = equation[0][2]
        right = (equation[0][0], '-', equation[2])
        
        return solving(variable,(left, '=', right))

def solvingMultiply(variable, equation) :
    if isInside(variable, equation[0][0]) :
        left = equation[0][0]
        right = (equation[2], '/', equation[0][2])

        return solving(variable,(left, '=', right))

    elif isInside(variable, equation[0][2]) :
        left = equation[0][2]
        right = (equation[2], '/', equation[0][0])
        
        return solving(variable,(left, '=', right))

def solvingDivide(variable, equation) :
    if isInside(variable, equation[0][0]) :
        left = equation[0][0]
        right = (equation[2], '*', equation[0][2])

        return solving(variable,(left, '=', right))

    elif isInside(variable, equation[0][2]) :
        left = equation[0][2]
        right = (equation[0][0], '/', equation[2])
        
        return solving(variable,(left, '=', right))

def solve (variable, equation) :
    if isInside(variable, equation[0]) :
        return solving (variable, equation)
    elif isInside(variable, equation[2]) :
        return solving(variable, (equation[2], equation[1], equation[0]))
    return None

def solving(variable, equation) :

    if variable == equation[0] :
        return equation
    op = (equation[0])[1]

    if op == '+' :
        return solvingAdd(variable, equation)
    elif op == '-' :
        return solvingSubtract(variable, equation)
    elif op == '*' :
        return solvingMultiply(variable, equation)
    elif op == '/' :
        return solvingDivide(variable, equation)

#
#  TESTS. Test the equation solver for CSci 1913 Lab 1.
#
#    James Moen
#    10 Sep 18
#
#  Every test is followed by a comment which shows what must be printed if your
#  code works correctly. It also shows how many points the test is worth, for a
#  total of 35 possible points.
#

print(isInside('x', 'x'))                          #  True   1 point
print(isInside('x', 'y'))                          #  False  1 point
print(isInside('x', ('x', '+', 'y')))              #  True   2 points
print(isInside('x', ('a', '+', 'b')))              #  False  2 points
print(isInside('+', ('a', '+', 'b')))              #  False  2 points
print(isInside('x', (('m', '*', 'x'), '+', 'b')))  #  True   2 points

print(solve('x', (('a', '+', 'x'), '=', 'c')))
#  ('x', '=', ('c', '-', 'a'))  2 points

print(solve('x', (('x', '+', 'b'), '=', 'c')))
#  ('x', '=', ('c', '-', 'b'))  2 points

print(solve('x', (('a', '-', 'x'), '=', 'c')))
#  ('x', '=', ('a', '-', 'c'))  2 points

print(solve('x', (('x', '-', 'b'), '=', 'c')))
#  ('x', '=', ('c', '+', 'b'))  2 points

print(solve('x', (('a', '*', 'x'), '=', 'c')))
#  ('x', '=', ('c', '/', 'a'))  2 points

print(solve('x', (('x', '*', 'b'), '=', 'c')))
#  ('x', '=', ('c', '/', 'b'))  2 points

print(solve('x', (('a', '/', 'x'), '=', 'c')))
#  ('x', '=', ('a', '/', 'c'))  2 points

print(solve('x', (('x', '/', 'b'), '=', 'c')))
#  ('x', '=', ('c', '*', 'b'))  2 points

print(solve('y', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('y', '=', (('m', '*', 'x'), '+', 'b'))  2 points

print(solve('x', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('x', '=', (('y', '-', 'b'), '/', 'm'))  2 points

print(solve('a', (('b', '+', 'c'), '=', ('d', '*', (('a', '/', 'e'), '-', 'f')))))
# ('a', '=', (((('b', '+', 'c'), '/', 'd'), '+', 'f'), '*', 'e'))  5 points