#Lab 2
#David Floeder
#I worked with Kenny Peng

def checks(string):
    if len(string) == 0:
        return 0
    x = 0
    index = 0
    while index < len(string):
        if '0' <= string[index] and string[index] <= '9':
            x += 1
            index += 1
        elif string[index] != ' ' and string[index] != ',':
            index += 1
            return 0
        else:
            index += 1
    if x == 0:
        return 0

def increments(L):
    x = len(L)
    if L[x - 1] == 9:
        L[x - 1] = 0
        while 0 <= x:
            if x - 1 == 0:
                L[0] = 0
                L.insert(0, 1)
                return L
            elif L[x - 2] == 9:
                return (increments(L[:-1]) + [L[x - 1]])
            else:
                L[x - 2] += 1
                return L
    else:
        L[x - 1] += 1
        return L

class Zillion:
    def __init__(self, digits):
        if checks(digits) == 0:
            raise RuntimeError
        else:
            length = len(digits)
            y = 0
            hold = []
            while y < length:
                if digits[y] == ' ':
                    y += 1
                elif digits[y] == ',':
                    y += 1
                else:
                    h = int(digits[y])
                    hold.append(h)
                    y += 1
            self.digits = hold
            
    def increment(self):
        self.digits = increments(self.digits)
        
    def isZero(self):
        x = 0
        y = 0
        z = self.digits
        while x < len(z):
            if z[x] == 0:
                 y = y
                 x += 1
            else:
                y += 1
                x += 1
        if y == 0:
            return True
        else:
            return False
            
    def toString(self):
        hold = self.digits
        string = ''
        x = 0
        while x < len(self.digits):
            string = string + str(self.digits[x])
            x += 1
        return string


#
#  TESTS. Test the class Zillion for CSci 1913 Lab 2.
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

