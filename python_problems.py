# From https://github.com/ProgrammingHero1/100-plus-python-coding-problems-with-solutions

# 1. Take two inputs from the user. One will be an integer. The other will be a float number. Then multiply them to display the output.

def int_float_multiply(int_num, float_num):
    return int_num * float_num

int_num = int(input("Give an integer: "))
float_num = float(input("Give a float: "))
print("Your result is: ", int_float_multiply(int_num, float_num))

# 2. Take two numbers from the users. Calculate the result of second number power of the first number.

def powered(num1, num2):
    return num1 ** num2

first_num = int(input("Give first number: "))
sec_num = int(input("Give second number: "))
print("Your result is: ", powered(first_num, sec_num))

# 3. 

