import types
import math

class Zillion:
 def __init__(self,digits):
  if type(digits) == types.StringType and len(digits) >= 1:
   count0 = 0
   flag = False
   while count0 < len(digits):
    if not digits[count0].isdigit():
     if not digits[count0] == ',':
      if not digits[count0] == ' ':
                        #print('E1')
       raise RuntimeError
    else:
     flag = True
    count0+=1
   if flag:
    #STR to List
    countOm = 0
    list = []
    length = len(digits)
    while countOm < length:
     list.insert(len(list),digits[countOm])
     countOm+=1
    self.__numlist = list
   else:
    raise RuntimeError
  else:
   raise RuntimeError
	###
 def increment(self):
    numeric = self.toInt() #takes list in __numList, and converts it into an Integer
    numeric += 1 #takes said Integer, adds one to it, the increment
    newList = self.toList(numeric) #takes incremented Integer and turns it into a new List
    self.__numlist = newList #takes new list and replaces the old list with list+1
 
 def toList(self,num):
     #Int to List
    numTemp = num
    numList = []
    length = 0
    countx = 0
    while numTemp > 0:
        numTemp = numTemp / 10
        length+=1
        countx+=1
    numTemp = num
    while numTemp > 0:
        numList.insert(0,str(numTemp % 10))
        numTemp  = numTemp / 10
    return numList

 def toInt(self):
    #List to Int
    endBase = len(self.__numlist)-1
    ex = 0
    num1 = 0
    while endBase >= 0:
        if self.__numlist[endBase].isdigit():
            #print((int(self.__numlist[endBase]) * (10^ex)))
            num1 += (int(self.__numlist[endBase]) * 10**ex)
            ex+=1
            endBase-=1
        else:
            endBase-=1
    return num1
        
 def toString(self):
     #List to String
		count3 = 0
		end = len(self.__numlist)
		comstr = ''
		while count3 < end:
			comstr += self.__numlist[count3]
			count3 += 1
		return comstr
 
 def isZero(self):
  #is it Zero? Changes nothing, just checks
  countz = 0
  trigger = True
  while countz < len(self.__numlist):
   if not self.__numlist[countz] == '0':
    if not self.__numlist[countz] == ' ':
     if not self.__numlist[countz] == ',':
      trigger = False
   countz += 1
  return trigger


###

# 	while count0 < len(digits):
#			print('#')
#			if :  #digits[count0] == types.IntType
#				nothing = nothing
				#all is good!
#			else:
#				print('E1')
#				raise RuntimeError
#			count+=1
###############################################################################
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
