#!/usr/bin/python3

def add_two(array):
    return [x + 2 for x in array]

array_num = [20, -5, 10, 26, 45]
sum_array = add_two(array_num)

print("Original array: ", array_num)
print("New array: ", sum_array)