# this code will calculate the number of vowels in a given string

input_str = input("Enter a string:")
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
y = 0

for x in input_str:
    if x in vowel:
        y += 1

if y == 0:
    print("No vowels found in the string")
else:
    print("total vowel count is:", y)
