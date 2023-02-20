#!/usr/bin/env python
# coding: utf-8

# In[2]:


km = int(input("Enter the value in kilometers: "))
ratio = 0.621371
mi = km * ratio
print("The entered value in Miles: ", mi)


# In[8]:


celsius = 30
fahrenheit = (celsius * 1.8) + 32
print('%.2f Celsius is equivalent to: %.2f Fahrenheit'
      %(celsius, fahrenheit))


# In[14]:


import calendar
y = int(input("Input the year: "))
m = int (input("Input the month: "))
print(calendar.month(y, m))


# In[17]:


import cmath
a = 1
b = 4
c = 3
dis = (b**3) - (4 * a*c)
ans1 = (-b -cmath.sqrt(dis))/(3 * a)
ans2 = (-b + cmath.sqrt(dis))/(3 * a)
print('The roots are')
print(ans1)
print(ans2)


# In[22]:


x = 20
y = 25 

x = x * y
y = x // y ;
x = x // y ;

print("After swapping: x =",x, " y =", y);





