"""Prog10. title() makes all first letter of each word in the string, capital letter.
And all other letter in small case. Create a program that do the same functionality
without using title() function."""

#define capitalization
def title(string):
    words = string.split()
    titled = [word.capitalize() for word in words]
    return " ".join(titled)

#ask input
user = title(input("Enter a string: "))

#print output
print(user)
