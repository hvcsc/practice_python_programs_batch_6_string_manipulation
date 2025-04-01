"""Prog10. rindex() return the first location of the function parameter in the string
starting from the last character. Create a program that do the same functionality
without using rindex() function."""

#ask input
user = input("Enter a string: ")
find = input("Enter the word to find: ")

#check rindex
position = -1
for i in range(len(user) - len(find), -1, -1):
    if user[i:i + len(find)] == find:
        position = i
        break

#print output
if position == -1:
    print("Not found")
else:
    print(f"\nPosition of '{find}': {position}")
