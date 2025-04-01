"""Prog09. index() return the first location of the function parameter in the string.
Create a program that do the same functionality without using index() function."""

#ask input
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
find = int(input("Enter the number to count: "))

#check first location
position = -1
for i in range(len(nums)):
    if nums[i] == find:
        position = i + 1
        break

#print location
print(f"\nPosition of {find}: {position}")