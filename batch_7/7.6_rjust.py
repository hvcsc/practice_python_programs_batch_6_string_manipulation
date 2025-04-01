"""Prog06. rjust() add space characters at the beginning of the string to complete the number
of characters specifies in function parameter. Create a program that do the same functionality
without using rjust() function."""

#define rjust
def r_just(string, width):
    return " " * (width - len(string)) + string

#ask input
string = input("Enter string: ")
width = int(input("Enter width: "))

#print output
print(r_just(string, width))