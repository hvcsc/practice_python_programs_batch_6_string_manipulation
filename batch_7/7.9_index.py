"""Prog09. index() return the first location of the function parameter in the string.
Create a program that do the same functionality without using index() function."""

#ask input
user = input("Enter a string: ")
find = input("Enter the character to find: ")

#check first location
position = user.find(find)

#print location
print(f"\nPosition of {find}: {position}")