#!/usr/bin/env python
# coding: utf-8

# In[2]:


def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;
num = 160;    
rem = sum = 0;    
len = calculateLength(num);  
n = num;    
while(num > 0):    
    rem = num%10;    
    sum = sum + int(rem**len);    
    num = num//10;    
    len = len - 1;    
    if(sum == n):    
        print(str(n) + " is a disarium number");    
else:    
    print(str(n) + " is not a disarium number");   


# In[11]:


def length_calculation(my_val):   
   len_val = 0   
   while(my_val != 0):   
      len_val = len_val + 1   
      my_val = my_val//10   
   return len_val   

def digit_sum(my_num):   
   remaining = sum_val = 0  
   len_fun = length_calculation(my_num)   
      
   while(my_num > 0):   
      remaining = my_num%10   
      sum_val = sum_val + (remaining**len_fun)   
      my_num = my_num//10  
      len_fun = len_fun - 1   
   return sum_val   
     
ini_result = 0  
    
print("The disarium numbers between 1 and 100 are : ") 
for i in range(1, 101):   
   ini_result = digit_sum(i)   
      
   if(ini_result == i):   
      print(i)


# In[20]:


def isHappy(n):    
    r = s = 0;    
    while(n > 0):    
        r = n%10    
        s += r**2  
        n //= 10    
    return s  
        
n = int(input())    
res = n;    
     
while(res != 1 and res != 4):    
    res = isHappy(res)    
     
if(res == 1):    
    print("happy number")
elif(res == 4):    
    print("not a happy number")


# In[25]:


import math
def digitsSquareSum(Number):
    Sum = rem = 0
    while Number > 0:
        rem = Number % 10
        Sum = Sum + math.pow(rem, 2)
        Number = Number // 10
    return Sum


minHpy = int(input("Enter the Minimum Happy Number = "))
maxHpy = int(input("Enter the Maximum Happy Number = "))

print("\nThe List of Happy Numbers from {0} and {1}".format(minHpy, maxHpy)) 
for i in range(minHpy, maxHpy + 1):
    Temp = i

    while Temp != 1 and Temp != 4:
        Temp = digitsSquareSum(Temp)

    if Temp == 1:
        print(i, end  = '  ')


# In[27]:


def checkHarshad( n ) :
    sum = 0
    temp = n
    while temp > 0 :
        sum = sum + temp % 10
        temp = temp // 10

    return n % sum == 0
if(checkHarshad(12)) : print("Yes")
else : print ("No")
 
if (checkHarshad(15)) : print("Yes")
else : print ("No")


# In[29]:


import math
print("Enter a range:")
range1=int(input())
range2=int(input())
print("Pronic numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
    flag = 0
    for j in range(0, i + 1):
        if j * (j + 1) == i:
            flag = 1
            break
    if flag == 1:
        print(i,end=" ")


# In[ ]:




