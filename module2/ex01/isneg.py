#!/usr/bin/python

number = int(input('Enter a number: '))
if (number < 0):
    print('This number is negative.')
elif (number == 0):
    print('This number is both positive and negative.')
else:
	print('This number is positive.')