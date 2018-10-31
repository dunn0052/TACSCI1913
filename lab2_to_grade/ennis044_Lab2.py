
# coding: utf-8

# In[24]:


class Zillion():
    def __init__(self, digits):
        self.num=[]
        hasnum=False
        for x in digits:
            for y in range (0,10):
                if str(y)==x:
                    self.num.append(y)
                    hasnum=True
            if x==' ':
                continue
            elif x==',':
                continue
            elif x.isdigit()!=True:
                 raise RuntimeError
        if hasnum!=True:
                raise RuntimeError
        
        
    def increment(self):
        
        def adding(x):
            if x>len(self.num):
                self.num.insert(0,1)
                
            elif self.num[-x]==9:
                self.num[-x]=0
                return adding(x+1)
            else:
                self.num[-x]+=1
                
        
        x=1
        return adding(x)
    
    def isZero(self):
        for x in self.num:
            if x!=0:
                return False
        return True
    
    def toString(self):
        
        def stringconversion(h,x):
            new=h+str(self.num[x])
            if x==(len(self.num)-1):
                return new
            else:
                return stringconversion(new,x+1)
        start=""
        counter=0
        return stringconversion(start,counter)
         
            
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

