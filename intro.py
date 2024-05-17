#this is my introduction to python in 2024. I hope to leran, write, debug and develop
#working applications using Python. 
#Hello world program in python. 

print("Hello world")


#Creating variables and assigning values. 

#To create a variable in python, all one needs to do is to specify the variable name and then assign a value to it. 

# ie. <variable name> = <value>

#Integers 

a = 25; 

print (a)

#Floating point 

pi = 3.142
print (pi)

#String 

name = 'Abel'

print(name)

#Boolean 

q = True

print (q) 

#Empty or Null datatype 

x = None

print (x)

#one cannot use python keywords as variable names. All python keywords can be accessed as: 

import keyword
print(keyword.kwlist)


#Rules of naming variables. 
'''
All variable names should either begin with a letter or an underscore (_)
Variable names can only consist of letters, numbers and underscores. 
Names are case sensitive

'''

#To see the type of datatype do: 

a = 3 

print(type(a))


# we can also assign multiple values in a single line in python 

b , c , d , e = 3, 4, 5, 6

print(b, c, d, e)

# we can also use cascading assignment where we assign a value to multiple names 


w = e = f = t = 1

print (w, e, f, t)

# When using such cascading assignment, it is important to note that all three variables a, b and c 
#refer to the same object in memory, an int object with the value of 1. 
#In other words, a, b and c are three different names given to the
#same int object. Assigning a different object to one of them afterwards doesn't change the others, just as expected:

#The above is also true for mutable types (like list, dict, etc.)
# just as it is true for immutable types (like int, string, tuple). 

x = y = [7, 5, 7]
y = [5, 7]

print (x , y)

x[0] = 45 # updating the value of x such that the first value is 45. 

print(y)

print (x)

#continue from page 35. 
#Day 1 Stats: total time used: 57 minutes. 
#Goal : At least do an hour of python per day consecutively for 6 months. 

