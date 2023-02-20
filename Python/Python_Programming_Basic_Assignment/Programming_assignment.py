#!/usr/bin/env python
# coding: utf-8

# In[1]:


print ("Hello Python")


# In[2]:


num1 = input('Enter first number: ')  
num2 = input('Enter second number: ')

# Add two numbers  
sum = float(num1) + float(num2)  
# Subtract two numbers  
min = float(num1) - float(num2)  
# Multiply two numbers  
mul = float(num1) * float(num2)  
#Divide two numbers  
div = float(num1) / float(num2)  
# Display the sum  
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  
  
# Display the subtraction  
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))  
# Display the multiplication  
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  
# Display the division  
print('The division of {0} and {1} is {2}'.format(num1, num2, div))  


# In[3]:


A = float(input('Enter first side: '))  
B = float(input('Enter second side: '))  
C = float(input('Enter third side: '))  
S = (A + B + C) / 2  

area = (S*(S-A)*(S-B)*(S-C)) ** 0.5  
print('The area of the triangle is %0.2f' %area) 


# In[16]:



x=10
y=50 

temp=x
x=y 
y= temp 

print("value of x:", x)
print("value of y:", y)


# In[17]:


import random 
list1 = [1,2,3,4,5,6]
print(random.choice(list1))
string = "striver"
print (random.choice(string))



