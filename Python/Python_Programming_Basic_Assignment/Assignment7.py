#!/usr/bin/env python
# coding: utf-8

# In[9]:


arr = []
arr = [12, 3, 4, 25]
ans = sum(arr)
print ('Sum of the array is ',ans)


# In[12]:


a = [20, 100, 10, 60, 5, 90, 11]
max_element = a[0]

for i in range(len(a)):
  if a[i] > max_element:
     max_element = a[i]

print (max_element)


# In[17]:


def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))


# In[23]:


def splitArr(arr, n, k): 
    for i in range(0, k): 
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
          
        arr[n-1] = x
arr = [10, 100, 5, 6, 25, 63]
n = len(arr)
position = 2
  
splitArr(arr, n, position)
  
for i in range(0, n): 
    print(arr[i], end = ' ')


# In[26]:


def ismonotone(a):
    n=len(a) 
    if n==1:
        return True
    else:
        if all(a[i]>=a[i+1] for i in range(0,n-1) or a[i]<=a[i+1] for i in range(0,n-1)):
            return True
        else:
            return False
A = [6, 5, 4, 2]
print(ismonotone(A))
b = [6, 2, 4, 2]
print(ismonotone(b))
c=[4,3,2]
print(ismonotone(c))
d=[1]
print(ismonotone(d))


# In[ ]:




