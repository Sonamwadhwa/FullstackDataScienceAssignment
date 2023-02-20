#!/usr/bin/env python
# coding: utf-8

# In[6]:


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1=min1+1


# In[8]:


x = 60
y = 120
if x > y:
  x, y = y, x
for i in range(1,x+1):
  if x%i == 0 and y%i == 0:
    hcf = i

print("HCF of", x, "and", y, "is:", hcf)


# In[9]:


dec = int(input("Enter an integer: "))
print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")


# In[10]:


print("Enter a String: ", end="")
text = input()
textlength = len(text)
for char in text:
    ascii = ord(char)
    print(char, "\t", ascii)


# In[11]:


def add(num1, num2):
    return num1 + num2
  
def subtract(num1, num2):
    return num1 - num2
  
def multiply(num1, num2):
    return num1 * num2
  
def divide(num1, num2):
    return num1 / num2
  
print("Please select operation -\n"         "1. Add\n"         "2. Subtract\n"         "3. Multiply\n"         "4. Divide\n")
  

select = int(input("Select operations form 1, 2, 3, 4 :"))
  
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
  
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
  
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
  
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
  
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")


# In[ ]:




