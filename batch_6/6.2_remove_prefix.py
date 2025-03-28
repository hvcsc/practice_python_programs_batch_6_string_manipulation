"""Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter.
Create a program that do the same functionality without using removeprefix() function."""

#get user input
user = input("Enter a string: ")

#set conditions
if " " in user:
    part = user.split(" ", 1)
    text = part[1]
else:
    text = ""

#print without the prefix
print(f"\nWithout prefix: {text}")