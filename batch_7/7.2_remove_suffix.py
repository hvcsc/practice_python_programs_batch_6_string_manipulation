"""Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter.
Create a program that do the same functionality without using removesuffix() function."""

#ask input
string = input("Enter string: ")
suffix = input("Enter suffix: ")

#remove suffix
if suffix.endswith(suffix):
    string = string[:len(suffix)]

#print output
print(string)