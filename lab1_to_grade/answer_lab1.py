#
#  SOLVE. Symbolically solve an equation for a variable.
#
#    James Moen
#    10 Sep 18
#
#  TOP SECRET, FOR CSCI 1913 TA's ONLY!
#

#  General comments:
#
#  0. There may be issues with Python 2 vs. Python 3. The code shown here
#  works on Python 2, which I have on my office computer.
#
#  1. Students might ask if they need to implement unary plus or minus. No.
#  Their code need only work on the four binary arithmetic operations. The
#  "elephant rule" is in effect: if there are no elephants in the problem, then
#  there are also no elephants in the solution.
#
#  2. Students might ask if they need to implement some kind of fancy interface
#  to read and write equations interactively. No. They might run their program
#  by calling SOLVE interactively (e.g., using the Python -i option), or from
#  PRINT statements (PRINT functions in Python 3). Or they might use some kind
#  of fancy IDE, but I don't know about those.
#
#  3. Students might ask how to construct a tuple using expressions, because I
#  don't think I did that in class; I think all my examples constructed tuples
#  using constants. Of course you just write the expressions separated by
#  commas and enclosed in parentheses (). A tuple with a single element needs
#  a redundant comma (x,) but they don't need to do that here.
#
#  4. Students may ask about the Python AND and OR operators. See IS INSIDE for
#  an example.
#
#  5. Students may try to modify the tuples that are passed to functions as
#  arguments. The assignment specifically says not to do that, and they can't
#  do it anyway, because tuples are immutable. The code is simpler without it!
#
#  6. There are many places in this program where I could have done error
#  checking. However, to keep things simple, students need only do an error
#  check in SOLVE. It's OK if students want to do more error checking than I
#  do, but sadly they don't get anything for it. Also complicated error checks
#  are likely to have errors themselves.
#
#  7. The file TESTS.PY contains tests for these functions. Students might copy
#  calls to the functions out of the tests, and paste them into the window in
#  which Python is running interactively. If students ask for examples of how
#  the functions are supposed to work, tell them to look at TESTS.PY.
#
#  8. The assignment says that students get ZERO POINTS for this assignment if
#  they use lists in any way. Some students won't read that, so make sure they
#  know. When you grade these, you'll have to make a quick check of their code
#  to make sure lists are not being used -- but all you need to do is look for
#  []'s with commas inside them. A smart text editor can do (some of) that.
#
#  9. Many students will want to use lists and then turn them into tuples. This
#  makes about as much sense as building a garage by first building a house,
#  then tearing it down to get the lumber. For this assignment I want them to
#  know the difference between lists and tuples, and this is one way to do it.
#
#  Please let me know as soon as possible if there are bugs, questions, or
#  some other problems.

import types

#  SOLVE. Solve the equation Q for the variable X.  X must appear either in the
#  LEFT or the RIGHT side of Q, but not in both sides. This really just sets up
#  SOLVING, which does all the work.
#
#  Note that they need not test if X appears in both sides of Q, even though
#  the program won't be able to solve Q if it does.

def solve(X, Q):
 if isInside(X, left(Q)):
  return solving(X, Q)
 elif isInside(X, right(Q)):
  return solving(X, (right(Q), '=', left(Q)))
 else:
  return None

#  IS INSIDE. Test if a variable X is inside expression E.
#
#  There is more than one way to write the IS INSTANCE test. Students should
#  get full credit for any such test that works. They should not use the IN
#  operator, as this will look at operators in tuples as well as the left and
#  right sides. Some students may want to use IN because they think it's cool,
#  but it's not relevant here. The type check might not work as shown in all
#  Pythons: I mentioned in lecture that there's more than one way to do it.

def isInside(X, E):
 if type(E) == tuple:
  return isInside(X, left(E)) or isInside(X, right(E))
 else:
  return X == E

#  SOLVING. Solve the equation Q for the variable X, which appears in L. The
#  dictionary SOLVER helps dispatch to a function chosen by the topmost
#  operator in Q's left side.
#
#  Students can decide which rule function to call either by using a dictionary
#  (as I did here) or by using an IF-ELIF-ELSE series. I think the dictionary
#  is cooler, but students don't know enough about them to do this yet.

def solving(X, Q):
 L = left(Q)
 if X == L:
  return Q
 else:
  return solver[op(L)](X, Q)

#  Here's what it looks like with IF-ELIF-ELSE's.
#
#  def solving(X, Q):
#   L = left(Q)
#   if X == L:
#    return Q
#   elif op(L) == '+':
#    return solvingAdd(X, Q)
#   elif op(L) == '-':
#    return solvingSubtract(X, Q)
#   elif op(L) == '*':
#    return solvingMultiply(X, Q)
#   elif op(L) == '/':
#    return solvingDivide(X, Q)
#   else:
#    return None

#  SOLVING ADD. Solve equation Q, of the form A + B = C, for variable X.
#
#  I used local variables A, B, C here so that my code would look like the four
#  rules in the lab handout. If students ask, then they should be encouraged to
#  do that too, because it may make their code easier to write.
#
#  There are symmetries between the four SOLVING XXX functions that aren't
#  mentioned in the handout, but that some clever students might discover.
#  For example, someone might realize that SOLVING ADD and SOLVING MULTIPLY
#  are really the same function, except for the operator. Similarly for SOLVING
#  SUBTRACT and SOLVING DIVIDE. They still have to write all four functions,
#  however, because the handout says so.

def solvingAdd(X, Q):
 A = left(left(Q))
 B = right(left(Q))
 C = right(Q)
 if isInside(X, A):
  return solving(X, (A, '=', (C, '-', B)))
 else:
  return solving(X, (B, '=', (C, '-', A)))

#  SOLVING SUBTRACT. Solve equation Q, of the form A - B = C, for variable X.
#
#  See grading notes for SOLVING ADD.

def solvingSubtract(X, Q):
 A = left(left(Q))
 B = right(left(Q))
 C = right(Q)
 if isInside(X, A):
  return solving(X, (A, '=', (C, '+', B)))
 else:
  return solving(X, (B, '=', (A, '-', C)))

#  SOLVING MULTIPLY. Solve equation Q, of the form A * B = C, for variable X.
#
#  See notes for SOLVING ADD.

def solvingMultiply(X, Q):
 A = left(left(Q))
 B = right(left(Q))
 C = right(Q)
 if isInside(X, A):
  return solving(X, (A, '=', (C, '/', B)))
 else:
  return solving(X, (B, '=', (C, '/', A)))

#  SOLVING DIVIDE. Solve equation Q, of the form A / B = C, for variable X.
#
#  See notes for SOLVING ADD.

def solvingDivide(X, Q):
 A = left(left(Q))
 B = right(left(Q))
 C = right(Q)
 if isInside(X, A):
  return solving(X, (A, '=', (C, '*', B)))
 else:
  return solving(X, (B, '=', (A, '/', C)))

#  SOLVER. Suppose we must solve an equation of the form A o B = C. Then SOLVER
#  maps the string 'o' to a function that solves that equation.
#
#  This need not appear if students implement SOLVING using IF-ELIF-ELSE's to
#  select which rule function to call. We can't make the dictionary until after
#  all four rule functions have been defined.

solver =                 \
 { '+': solvingAdd,      \
   '-': solvingSubtract, \
   '*': solvingMultiply, \
   '/': solvingDivide }

#  Students should be encouraged to use LEFT, OP, and RIGHT instead of the
#  goofy bracket postfix operator to select the parts of expressions. It makes
#  their code much easier to read that way, and it's less prone to error.

#  LEFT. Return expression E's left argument, a tuple or a string.

def left(E):
 return E[0]

#  OP. Return expression E's operator, a string.

def op(E):
 return E[1]

#  RIGHT. Return expression E's right argument, a tuple or a string.

def right(E):
 return E[2]
