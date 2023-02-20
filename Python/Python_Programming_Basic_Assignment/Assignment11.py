#!/usr/bin/env python
# coding: utf-8

# In[29]:


def word_k(k, s):    
    word = s.split(" ")
    for x in word:
        if len(x)>k:
          print(x)
k = 3
s ="Python is good"
word_k(k, s)


# In[30]:


def remove_char(s, i):
    a = s[ : i]
    b = s[i + 1: ]
return a+b
string = "Pythonisgood"
i = 5
print(remove_char(string,i-1))


# In[1]:


def split_string(string):
    list_string = string.split(' ')
    return list_string

def join_string(list_string):
    string = '-'.join(list_string)
    return string

string = 'Welcome to Ineuron'
list_string = split_string(string)
print("After Splitting: ",list_string)
res_string = join_string(list_string)
print("After joining: ",res_string)


# In[2]:


def uncomn_wrd(x,y):
    x = x.split()
    y = y.split()
    k = set(x).symmetric_difference(set(y))
    return k


str1 = input("Enter first string : ")
str2 = input("Enter second string : ")
print("Uncommon words are :", list(uncomn_wrd(str1, str2)))


# In[4]:


string = input("enter the string whose duplicate characters you want to find:")

def duplicates_char(s):
    elements = {}
    for char in s:
        if elements.get(char,None) != None:
            elements[char]+=1
        else:
            elements[char] = 1
    return [k for k,v in elements.items() if v>1]
print("the duplicate character in",string)
print(duplicates_char(string))


# In[6]:


myStr =  input('Enter the binary string : ')
flag = True
for char in myStr :
    if(char == '0' or char == '1'):
       continue 
    else :
        flag = False
        print("The String is not a binary string")
        break
    
if(flag):
    print("The String is binary string")


# In[1]:


import re
myStr =  input('Enter the string : ')
regularExp = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
print("Entered String is ", myStr)
if(regularExp.search(myStr) == None):
    print("The string does not contain special character(s)")
else:
    print("The string contains special character(s)")


# In[ ]:




