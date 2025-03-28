"""Prog06. ljust() add space characters at the end of the string to complete the number of characters
specifies in function parameter. Create a program that do the same functionality without using ljust() function."""

#define ljust
def l_just(string, width):
    return string + " " * (width - len(string))

#ask user for input
string = input("Enter string: ")
width = int(input("Enter width: "))

#print output
print(l_just(string, width))
