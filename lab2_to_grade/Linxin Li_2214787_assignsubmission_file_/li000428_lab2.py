class Zillion:

	def __init__ (self,digits):
		if digits == '':
			raise RuntimeError
		self.list = []
		other = 0
		for i in digits:
			if i == ',' or i == ' ':
				self.list = self.list
			else:
				try:
					if type(int(i)) == int:
						self.list = self.list + [int(i)]
						other += 1
				except:
					raise RuntimeError
			
		if other == 0:
			raise RuntimeError
	
	def increment(self):
		for index in range(len(self.list) -1,-1,-1):
			if self.list[index] == 9:
				self.list[index] = 0
			else:
				self.list[index] += 1
				return None
		if self.list[0] == 0:
			self.list = [1] + self.list
		
				
	def isZero(self):
		if self.list == '':
			return False
		count = 0
		x = 0
		while x < len(self.list):
			if self.list[x] == 0:
				count += 1
			x += 1
		return count == len(self.list)
		
	def toString(self):
		string = ''
		for digit in self.list:
			string += str(digit)
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
			
		
			
			
			
			
			
