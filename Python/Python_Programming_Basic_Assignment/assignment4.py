#!/usr/bin/env python
# coding: utf-8

# In[2]:


def factorial(n):
return 1 if (n==1 or n==0) else n * factorial(n - 1);
num = 6;
print("Factorial of",num,"is",
factorial(num))


# In[3]:


number = int(input("enter the number:"))
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
    print (number, 'x', count, '=', number * count)


# In[13]:


n = int(input("Enter the value of 'n':"))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ",end=" ")
while(count <= n):
  print(sum,end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b


# In[25]:


number = 200
temp = number
add_sum = 0
while temp!=0:
    k = temp%10
    add_sum +=k*k*k
    temp = temp//10
if add_sum==number:
    print('Armstrong Number')
else:
    print('Not a Armstrong Number')


# In[36]:


num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# In[38]:


num = 21

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)

