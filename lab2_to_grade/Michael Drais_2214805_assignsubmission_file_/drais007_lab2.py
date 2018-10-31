#Micahel Drais
# section 4
# 18/9/18
#lab2



class Zillion:
	def __init__(self, digits):
		self.nums = []
		for d in digits:
			if((d == ',') or (d == ' ')):
				#print(" unnecisary item")
				continue
			elif((d == '0') or (d == '1') or (d == '2') or (d == '3') or (d == '4') or (d == '5') or (d == '6') or (d == '7')or (d == '8') or (d == '9')):
				#print ("digit")
				self.nums.append(int(d))
			else:
				#print ('error')
				raise RuntimeError
		if (len(self.nums) == 0):
			#print ('no items')
			raise RuntimeError		 
		self.nums.reverse()		
			
	def increment(self):
		index = 0;
		while (index < len(self.nums)):
			if (self.nums[index] == 9):
				self.nums[index] = 0
				index += 1
			else:
				self.nums[index] += 1
				return
		self.nums.append(1)			
	def isZero(self):
		for n in self.nums:
			if(n != 0):
				return False
		
		return True		
	def toString(self):
		st = ""
		for i in reversed(self.nums):
			st += str(i)
		
		return st	
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
