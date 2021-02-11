# !/usr/bin/python3
# Calculator Program
# Programmer : PMH
# Date       : 2/4/2021

first_num = float(input("Enter 1st number: "))
operator = input("Enter operator: ")
second_num = float(input("Enter 2nd number: "))
result = 0

if operator == '+':
    result = first_num + second_num
elif operator == '-':
    result = first_num - second_num
elif operator == '*':
    result = first_num * second_num
elif operator == '/':
    result = first_num / second_num
elif operator == '%':
    result = first_num % second_num
elif operator == '//':
    result = first_num // second_num
elif operator == '**':
    result = first_num ** second_num
else:
    print("Wrong Operator!")
print("The Result is: ", result)
print()
print("~~~ Thanks For Using! ~~~")
