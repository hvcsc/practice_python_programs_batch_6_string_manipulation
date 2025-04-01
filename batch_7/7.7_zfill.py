"""Prog07. zfill() add zero characters at the beginning of the string to complete the number
of characters specifies in function parameter. Create a program that do the same functionality
without using zfill() function."""

#ask input
num = int(input("Enter a number: "))
form = int(input("Enter number format: "))

#change format
num = f"{num:0{form}d}"

#print format
print(f"\nOutput: {num}")
