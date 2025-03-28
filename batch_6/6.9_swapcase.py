"""Prog09. swapcase() reverse the casing of each of the character of the string.
Create a program that do the same functionality without using swapcase() function."""

#define condition for swapcase
def swap_case(string):
    swap = ""
    for i in string:
        if i.islower():
            swap += i.upper()
        elif i.isupper():
            swap += i.lower()
        else:
            swap += i
    return swap

#ask input
user = swap_case(input("Enter string: "))

#print
print(user)