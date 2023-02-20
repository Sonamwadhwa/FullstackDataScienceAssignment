#!/usr/bin/env python
# coding: utf-8

# In[16]:


def putNumbers(n):

    i = 0

    while i<n:

        j=i

        i=i+1

        if j%7==0:

            yield j
for i in putNumbers(100):

    print (i)


# In[32]:


import operator

text_line = input("Type in: ")

freq_dict = {}

for i in text_line.split(' '):
    if i.isalpha():
        if i not in freq_dict:
            freq_dict[i] = 1
        elif i in freq_dict:
            freq_dict[i] = freq_dict[i] + 1
    else:
        pass

sorted_freq_dict = sorted(freq_dict.items(), key = operator.itemgetter(0))
print(sorted_freq_dict)

for i in sorted_freq_dict:
    print(i[0], i[1])


# In[40]:


class  Person(object):  
    def  getGender(  self  ):  
        return  "Unknown"  
class  Male(  Person  ):  
    def  getGender(  self  ):  
        return  "Male"  
class  Female(  Person  ):  
    def  getGender(  self  ):  
        return  "Female"  

aMale  =  Male()  
aFemale=  Female()  
print(aMale.getGender())  
print  (aFemale.getGender())


# In[45]:


subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]

res = [[i, j, k] for i in subjects  
                 for j in verbs 
                 for k in objects] 
for x in res:
    print(" ".join(x))


# In[43]:


import zlib
s = 'hello world!hello world!hello world!hello world!'.encode()
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))


# In[3]:


def binary_search_Ascending(array, target):
    lower = 0
    upper = len(array)
    print('Array Length:',upper)
    while lower < upper:
        x = (lower + upper) // 2
        print('Middle Value:',x)
        value = array[x]
        if target == value:
            return x
        elif target > value:
            lower = x
        elif target < value:
            upper = x

Array = [1,5,8,10,12,13,55,66,73,78,82,85,88,99]
print('The Value Found at Index:',binary_search_Ascending(Array, 82)) 


# In[ ]:




