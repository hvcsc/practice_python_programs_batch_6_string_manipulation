"""Prog04. islower() check if all characters of the string is on lower case.
Create a program that do the same functionality without using islower() function."""

#ask input
user = input("Enter string: ")

#check if lower and print
if user == user.casefold():
    print("True")
else:
    print("False")