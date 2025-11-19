# this program demontrates various operations of strings in python

name = "Cobalt"
reverse = name[:: -1]
print(name[0], name[5])  # prints first and last char of the string
print(reverse)  # prints reversed string
print("Coba\nlt")  # prints name with escape sequence
print(f"Hello, {name}!, your name in reverse is {reverse}")
print(name[1:4])
