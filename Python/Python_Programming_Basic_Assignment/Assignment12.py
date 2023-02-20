#!/usr/bin/env python
# coding: utf-8

# In[1]:


myDict =myDict = {'Scala': 2, 'Javascript': 1, 'Python': 8, 'C++': 1, 'Java': 4}
uniqueValues = list({val for val in myDict.values() })
print("Dictionary = ", end = " ")
print(myDict)
print("Unique Values = ", end = " ")
print(uniqueValues)


# In[3]:


def returnSum(myDict):
     list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
 
    return final

dict = {'a': 500, 'b': 100, 'c': 400}
print("Sum :", returnSum(dict))


# In[8]:


dict_1 = {'John': 15, 'Rick': 10, 'Misa' : 12 }
dict_2 = {'Bonnie': 18,'Rick': 20,'Matt' : 16 }
dict_1.update(dict_2)
print('Updated dictionary:')
print(dict_1)


# In[16]:


def test(flat_dict):
     return list(flat_dict.keys())
students = {
  'Theodore': 19,
  'Roxanne': 20,
  'Mathew': 21,
  'Betty': 20
}

print("\n Original dictionary elements:")
print(students)
print("\n Create a flat list of all the keys of the said flat dictionary:")
print(test(students))


# In[2]:


from collections import OrderedDict
dic1 = OrderedDict([('A', '100'), ('B', '200'), ('C', '300')])
insrt = OrderedDict([("D", '400')])
  
final = OrderedDict(list(insrt.items()) + list(dic1.items()))
print ("Resultant Dictionary :")
print(final)


# In[13]:


import collections

ordered_dict = collections.OrderedDict()

ordered_dict['1'] = "one"
ordered_dict['2'] = "two"
ordered_dict['3'] = "three"
ordered_dict['4'] = "four"
ordered_dict['5'] = "five"

print("Printing Ordered Dictionary : ")

for key,value in ordered_dict.items():
	print("key : {0},value : {1}".format(key,value))


# In[16]:


key_value={}

key_value[5] = 10      
key_value[3] = 8
key_value[6] = 77
key_value[4] = 23
key_value[2] = 9     
key_value[1] = 43
 
print("sorting on the basis of keys")
for i in sorted(key_value) :
    print ((i, key_value[i]), end =" ")


# In[ ]:




