#!/usr/bin/python3

first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
result = first_number * second_number

if (result < 0):
    print(first_number, ' x ', second_number, ' = ', result)
    print('The result is negative.')
elif (result == 0):
    print(first_number, ' x ', second_number, ' = ', result)
    print('The result is positive and negative.')
else:
    print(first_number, ' x ', second_number, ' = ', result)
    print('The result is positive.')