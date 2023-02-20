#!/usr/bin/env python
# coding: utf-8

# In[2]:


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 12

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# In[13]:


def recursive_factorial(n):
  if n == 1:
     return n
  else:
     return n*recursive_factorial(n-1)     

number = int(input("User Input : "))
print("The factorial of", number, "is", recursive_factorial(number))


# In[14]:


height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))


# In[16]:


import math
number = int(input("Enter the number: "))
ans = math.log(number)
print("The value is:",ans)


# In[20]:


def sumOfSeries(n):
    x = (n * (n + 1)  / 2)
    return (int)(x * x)
n = 6
print(sumOfSeries(n))


# In[ ]:




