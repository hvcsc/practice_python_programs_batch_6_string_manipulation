"""Prog09. capitalize() makes the first letter of the string, capital letter.
And all other letter in small case. Create a program that do the same functionality
without using capitalize() function."""

#ask input
string = input("Enter statement: ")
string = string[0].upper() + string[1:].lower()

#print output
print(string)
