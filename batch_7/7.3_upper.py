"""Prog03. upper() converts all characters of the string into upper case.
Create a program that do the same functionality without using upper() function."""

#ask input
user = input("Enter string: ").lower()

#convert to upper
upper = user.swapcase()

#print output
print(upper)