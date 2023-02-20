**BASIC PROGRAMMING ASSIGNMENT17**

Question1. Create a function that takes three arguments a, b, c and returns the sum of the
numbers that are evenly divided by c from the range a, b inclusive.
Examples 
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.
evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
"""

def sumDivisibles(a, b, c):     
    sum = 0
    for i in range(a, b + 1): 
        if (i % c == 0):
            sum += i 
    return sum
a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))
print(sumDivisibles(a, b, c))

Question2. Create a function that returns True if a given inequality expression is correct and
False otherwise.
Examples
correct_signs(&quot;3 &lt; 7 &lt; 11&quot;) ➞ True
correct_signs(&quot;13 &gt; 44 &gt; 33 &gt; 1&quot;) ➞ False
correct_signs(&quot;1 &lt; 2 &lt; 6 &lt; 9 &gt; 3&quot;) ➞ True 
"""

def correct_signs ( txt ) : 
    return eval ( txt )
print(correct_signs("3 > 7 < 11"))
print(correct_signs("13 > 44 > 33 > 1"))
print(correct_signs("1 < 2 < 6 < 9 > 3"))

Question3. Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels(&quot;the aardvark&quot;, &quot;#&quot;) ➞ &quot;th# ##rdv#rk&quot;
replace_vowels(&quot;minnie mouse&quot;, &quot;?&quot;) ➞ &quot;m?nn?? m??s?&quot;
replace_vowels(&quot;shakespeare&quot;, &quot;*&quot;) ➞ &quot;sh*k*sp**r*&quot;
"""

def replace_vowels(str, s):
    vowels = 'AEIOUaeiou'
    for ele in vowels:  
        str = str.replace(ele, s)  
    return str
  
input_str = input("enter a string : ")
s = input("enter a vowel replacing string : ")
print("\nGiven Sting:", input_str)
print("Given Specified Character:", s)
print("Afer replacing vowels with the specified character:",replace_vowels(input_str, s))

Question4. Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1
"""

def factorial(n):     
    if n == 0:
        return 1    
    return n * factorial(n-1)

num = int(input('enter a number :'))
print("Factorial of", num, "is", factorial(num))

QUES 5. Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: &quot;abcbba&quot;
String2: &quot;abcbda&quot;
Hamming Distance: 1 - &quot;b&quot; vs. &quot;d&quot; is the only difference.
"""

def hamming_distance(str1, str2):
    i = 0
    count = 0
 
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count
 
# Driver code 
str1 = "abcde"
str2 = "bcdef"
 
# function call
print(hamming_distance(str1, str2))

print(hamming_distance('abcbba', 'abcbda'))

hamming_distance('abcde', 'abcde')