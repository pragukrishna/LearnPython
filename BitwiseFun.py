# this is a fun Bitwise puzzle

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Bitwise AND:", num1 & num2)
print("Bitwise OR:", num1 | num2)
print("Bitwise XOR:", num1 ^ num2)
print("left shift of num1: ", num1 << 1)
print("right shift of num2: ", num2 >> 1)
print("one'e complement of num1:", ~num1)
