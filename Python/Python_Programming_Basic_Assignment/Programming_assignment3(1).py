#!/usr/bin/env python
# coding: utf-8

# In[16]:


num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")


# In[18]:


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# In[20]:


year = 2001
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))


# In[41]:


print("Enter the Number: ")
num = int(input())
p = 0
for i in range(2, num):
    if num%i==0:
        p = 1
        break
if p==0:
    print("\n It is a Prime Number")
else:
    print("\n It is not a Prime Number")


# In[42]:


lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print(number)  


# In[ ]:




