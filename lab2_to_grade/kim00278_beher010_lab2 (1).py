
class Zillion:
	
	def __init__(self, digits):
		dig = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
		symb = (',', ' ')
 	 	self.__digits = digits
        	i = 0
		self.list = []
		while(i < len(self.__digits)):
			if self.__digits[i] in dig:
				self.list.append(int(self.__digits[i]))
				i+=1
			elif self.__digits[i] in symb:
				i+=1
			else:
				raise RuntimeError
		if self.list == []:
			raise RuntimeError
	def increment(self):
		for x in range(len(self.list) - 1, -1, -1):
			if self.list[x] == 9:
				self.list[x] = 0
			else:
				self.list[x] = self.list[x] + 1
				return None
		self.list = [1] + self.list
    
	def isZero(self):
		for x in self.list:
			if x != 0:
				return False
		return True

	def toString(self):
		string = ""
		for number in self.list:
			string = string + str(number)
		return string
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


print(Zillion('0').isZero())    #  It must print True. 2 points.

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
