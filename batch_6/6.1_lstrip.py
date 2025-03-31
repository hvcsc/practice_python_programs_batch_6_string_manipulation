"""Prog01. lstrip() remove the space characters at the beginning of the string.
Create a program that do the same functionality without using lstrip() function."""

#ask input
string = input("Enter string: ")

#remove space
while string.startswith(" "):
    string = string[1:]

#print output
print(string)