def splitDigits(digs):
    def explode(str):
        a = []
        for x in str:
            a += [x]
        return a

    def verify(charList):
        acceptableChars = [',', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if not charList:
            raise RuntimeError
        oneDigit = False
        for x in charList:
            if x not in acceptableChars:
                raise RuntimeError
            elif x in acceptableChars[2:]:
                oneDigit = True
        if not oneDigit:
            raise RuntimeError
        return charList


    def strsToInts(strs):
        b=[]
        for x in strs:
            if x == '':
                b += [0]
            elif x != ',' and x != ' ':
                b+= [int(x)]
        return b

    return strsToInts(verify(explode(digs)))



class Zillion:
    def __init__(self, digits):
        self.digits = splitDigits(digits)

    def increment(self):
        def helper(self, position):
            if position < 0:
                self.digits = [1] + self.digits
            elif self.digits[position] == 9:
                self.digits[position] = 0
                helper(self, position - 1)
            else:
                self.digits[position] += 1

        helper(self, len(self.digits) - 1)

    def isZero(self):
        for x in self.digits:
            if x != 0:
                return False
        return True

    def toString(self):
        ret = ""
        for x in self.digits:
            ret += str(x)
        return ret



#
#  TESTS. Test the class Zillion for CSci 1913 Lab 2.
#
#    James Moen
#    18 Sep 17
#
#  Every test is followed by a comment which shows what must be printed if your
#  code works correctly. It also shows how many points the test is worth.
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
