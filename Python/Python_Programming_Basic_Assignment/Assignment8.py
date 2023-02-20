#!/usr/bin/env python
# coding: utf-8

# In[4]:


A = [[15,7,3],

    [4 ,5,6],

    [7 ,8,10]]

B = [[7,8,3],

    [7,7,4],

    [5,7,9]]

result = [[0,0,0],

         [0,0,0],

         [0,0,0]]

for x in range(len(A)):
    for y in range(len(A[0])):
        result[x][y] = A[x][y] + B[x][y]
for q in result:
      print(q)


# In[22]:


A = [[5, 4, 3],  
     [2, 4, 6],  
     [4, 7, 9]]    
B = [[3, 2, 4],  
     [4, 3, 6],  
     [2, 7, 5]]   
multiResult = [[0, 0, 0],    
               [0, 0, 0],    
               [0, 0, 0]]  
for m in range(len(A)):    
    for n in range(len(B[0])):    
          for o in range(len(B)):    
                multiResult[m][n] += A[m][o] * B[o][n] 
print("The multiplication result of matrix A and B is: ")  
for res in multiResult:    
    print(res)  


# In[23]:


A = [[5, 4, 3],  
    [2, 4, 6],  
    [4, 7, 9],  
    [8, 1, 3]]  
transResult = [[0, 0, 0, 0],    
               [0, 0, 0, 0],  
               [0, 0, 0, 0]]  
for a in range(len(A)):    
    for b in range(len(A[0])):    
          transResult[b][a] = A[a][b] 
print("The transpose of matrix A is: ")  
for res in transResult:    
     print(res)  


# In[1]:


input_str = input("Enter a string: ")

words = input_str.split()
words.sort()

print("The sorted words are:")
for word in words:
    print(word)


# In[33]:


def Punctuation(string):
 
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
    
    for x in string.lower():
        if x in punctuations:
            string = string.replace(x, "")
    print(string)
 
string = "Welcome???@@##$ to#$% Ineuron%$^ Data$%^&Science"
Punctuation(string)