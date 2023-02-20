#!/usr/bin/env python
# coding: utf-8

# In[3]:


arr = []
arr = [12, 3, 14,15]
ans = sum(arr)
print('Sum of the array is ',ans)


# In[11]:


import array as arr
a = arr.array('i',[3, 24, 11, 40])
print (' Greatest element in the array is ', max(a) ) 


# In[3]:


list1 = [30, 20, 6, 45, 99]
list1.sort()
print("Smallest element is:", *list1[:1])


# In[5]:


list = [1, 50, 40, 36, 16]
list.sort()
print("Largest number in the list is:", list[-1])


# In[6]:


list = [1, 50, 40, 36, 16]
list.sort()
print("Largest number in the list is:", list[-2])


# In[8]:


def Nmaxelements(list1, N):
    final_list = []
 
    for i in range(0, N): 
        max1 = 0
         
        for j in range(len(list1)):     
            if list1[j] > max1:
                max1 = list1[j];
                 
        list1.remove(max1);
        final_list.append(max1)
         
    print(final_list)
 
list1 = [2, 6, 41, 85, 100, 5, 7, 6, 10]
N = 2
Nmaxelements(list1, N)


# In[1]:


def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# In[5]:


def is_odd_num(l):
    odd = []
    for n in l:
        if n % 2 != 0:
            odd.append(n)
    return odd
print(is_odd_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# In[8]:


listofList = [[5], [54, 545,9], [], [1, 4, 7], [], [8, 2, 5] ]
print("List of List = ", end = " ")
print(listofList)
nonEmptyList = [] 
nonEmptyList = list(filter(None, listofList))
print("List without empty list: ", end = " " )
print(nonEmptyList)


# In[10]:


li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Original list: ",li)
list_copy = li[:]
print("After cloning: ",list_copy)


# In[12]:


sample_list = [3,7,8,9,3,6,7,3,10,3,10,3]
count = sample_list.count(3)
print("Count of 3 in sample list is:", count)


# In[ ]:




