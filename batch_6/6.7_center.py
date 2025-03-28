"""Prog07. center() add space characters at the beginning and at the end of the
string to print the string at the center. Create a program that do the same functionality
without using center() function."""

#define center()
def center(string, width):
    spaces = (width - len(string)) // 2
    return ' ' * spaces + string + ' ' * (width - len(string) - spaces)

#ask input
user = input("Enter a string: ")
wid = int(input("Enter the total width: "))

#print output
print(center(user, wid))