"""Prog05. endswith() check if the string end part matches the function parameter.
Create a program that do the same functionality without using endswith() function."""

#define suffix
def ends_with(string, suffix):
    position = len(string) - len(end)
    if string.find(end, position) == position:
        return True
    else:
        return False

#user input
string = input("Enter a string: ")
end = input("\nEnter the suffix to check: ")

#call function and print
if ends_with(string, end):
    print("\nTrue")
else:
    print("\nFalse")