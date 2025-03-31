"""Prog01. rstrip() remove the space characters at the end of the string.
Create a program that do the same functionality without using rstrip() function."""

#ask user input
user = input("Enter a string with space characters at the end: ")

#remove space characters at the end
while user.endswith(" "):
    user = user[:-1]

#print output
print(user)