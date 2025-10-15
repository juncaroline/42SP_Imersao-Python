#!/usr/bin/python3

first_number = int(input('Give me the first number: '))
second_number = int(input('Give me the second number: '))
print('Thank you!')
print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
if (second_number == 0):
    print("Division by zero is not allowed")
else:
    result = first_number / second_number
    if result.is_integer():
        print(f"{first_number} / {second_number} = {int(result)}")
    else:
        print(f"{first_number} / {second_number} = {result}")
print(f"{first_number} * {second_number} = {first_number * second_number}")