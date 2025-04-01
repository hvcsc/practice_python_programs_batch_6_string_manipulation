"""Prog08. count() return how many time the function parameter appear in the string.
Create a program that do the same functionality without using count() function."""

#ask input
string = input("Enter a string: ")
sub = input("Enter the substring to count: ")

#count
count = 0
for i in range(len(string) - len(sub) + 1):
    if string[i:i + len(sub)] == sub:
        count += 1

#print count
print(f"\nCount: {count}")