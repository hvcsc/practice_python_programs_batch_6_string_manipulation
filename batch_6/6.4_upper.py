"""Prog04. isupper() check if all characters of the string is on upper case.
Create a program that do the same functionality without using isupper() function."""

#ask input
user = input("Enter a string: ")

#check if upper and print
if user.islower():
    print("False")
else:
    print("True")