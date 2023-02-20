#!/usr/bin/env python
# coding: utf-8

# In[9]:


def generate(n):
    for i in range(n+1):
        if i % 35 == 0:    
            yield i

n = int(input())
resp = [str(i) for i in generate(n)]
print(",".join(resp))


# In[15]:


n = int(input())

for i in range(0, n+1, 2):
  if i < n - 1:
    print(i, end = ',' )
  else:
    print(i)


# In[19]:


def f(n):
    if n < 2:
        fibo[n] = n
        return fibo[n]
    fibo[n] = f(n-1) + f(n-2)
    return fibo[n]

n = int(input())
fibo = [0]*(n+1)  
f(n)              
fibo = [str(i) for i in fibo]  
ans = ",".join(fibo)    
print(ans)


# In[41]:


import re
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(1))


# In[43]:


class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

Asqr = Square(5)
print(Asqr.area())      

print(Square().area())  


# In[ ]:




