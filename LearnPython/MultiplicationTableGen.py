#this code will generate the multiplication table for an inputted number


def gen_multiplication_table(num):
    mul_table = []
    for i in range(1,11):
        mul_table.append(num * i)
    print(mul_table)
        

number = int(input("Enter a number you would want the multiplication table for:"))
gen_multiplication_table(number)