#Taking user input in python
# Write a program that asks the user for their name, age, 
#and location and then prints out a personalized message.

name = str(input("Please enter your name: "))
age = int(input('Please enter your age: '))
location = input('Enter your location address: ')

print('Hello '+ name + ', you are '+ str(age) +' years old, and live in '+ location + '.')
