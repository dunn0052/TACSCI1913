#
#  ZILLION. A counter supporting arbitrarily many decimal digits, without using
#  Python's "long" integers.
#
#    James B. Moen
#    20 Sep 17
#
#  TOP SECRET FOR CSCI 1913 TA's ONLY!
#

#  ZILLION. An "infinite" length counter.
#
#  Like it says in the assignment, they get 0 (yes, that's zero) points if they
#  use Python's arbitrary-length "long" integers in any way. For example, they
#  can't convert the list of digits to a string, then convert the string to a
#  long, and finally operate on that. They must demonstrate some understanding
#  of lists and class methods, etc.

class Zillion:

#  INIT. Initialize the counter with a string of digits.
#
#  They should call INT to convert digits to integers, but it's OK if they
#  don't and their code still works somehow. It's also OK if they make two
#  or more passes through the string -- maybe one checks for errors, and the
#  other actually does the work.

 def __init__(self, digits):
  found = False
  self.digits = []
  for digit in digits:
   if '0' <= digit and digit <= '9':
    found = True
    self.digits += [int(digit)]
   elif digit == ' ' or digit == ',':
    pass
   else:
    raise RuntimeError
  if not found:
   raise RuntimeError

#  INCREMENT. Add 1 to the counter.

 def increment(self):
  index = len(self.digits) - 1
  while index >= 0 and self.digits[index] == 9:
   self.digits[index] = 0
   index -= 1
  if index < 0:
   self.digits = [1] + self.digits
  else:
   self.digits[index] += 1

#  TO STRING. Convert the counter to a string and return it.
#
#  This is intended to be easy, and is here so that almost everyone will get
#  some points. They should use STR to convert digits to strings, but it's OK
#  if they don't and their code still works somehow.

 def toString(self):
  digits = ''
  for digit in self.digits:
   digits += str(digit)
  return digits

#  IS ZERO. Test if the counter is 0.
#
#  In previous semesters, I made them use REDUCE here. Unfortunately my lecture
#  schedule is different now, so I probably won't have done REDUCE by the time
#  they see this. They can use REDUCE if they know it, but here I've used a
#  loop.

 def isZero(self):
  for digit in self.digits:
    if digit != 0:
      return False
  return True

#
#  TESTS. Test the class Zillion for CSci 1913 Lab 2.
#
#    James B. Moen
#    30 Jan 17
#
#  Every test is followed by a comment which shows what must be printed if your
#  code works correctly. It also shows how many points the test is worth, for a
#  total of 35 possible points.
#

try:
  z = Zillion('')
except RuntimeError:
  print('Empty string')

# It must print 'Empty string' without apostrophes. 2 points.

try:
  z = Zillion(' , ')
except RuntimeError:
  print('No digits in the string')

# It must print 'No digits in the string' without apostrophes. 2 points.

try:
  z = Zillion('1+0')
except RuntimeError:
  print('Non-digit in the string')

# It must print 'Non-digit in the string' without apostrophes. 2 points.

try:
  z = Zillion('0')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
  z = Zillion('000000000')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
  z = Zillion('000 000 000')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
  z = Zillion('997')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing.  2 points.

print(z.isZero())    #  It must print False. 2 points.

print(z.toString())  #  It must print 997. 2 points.

z.increment()

print(z.toString())  #  It must print 998. 2 points.

z.increment()

print(z.toString())  #  It must print 999. 2 points.

z.increment()

print(z.toString())  #  It must print 1000. 2 points.

try:
  z = Zillion('0 9,9 9')
except:
  print('This must not be printed')

#  It must print nothing.  3 points.

z.increment()
print(z.toString())  #  It must print 1000. 2 points.
