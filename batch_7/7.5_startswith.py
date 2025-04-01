"""Prog05. startswith() check if the string beginning part matches the function parameter.
Create a program that do the same functionality without using startswith() function."""

#ask input
string = input("Enter string: ")
start = input("Enter prefix: ")

#check conditions
if string[:len(start)] == start:
    print("True")
else:
    print("False")