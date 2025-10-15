#!/usr/bin/python3

def add_two(array):
    return [x + 2 for x in array if x > 5]

array_num = [20, -5, 20, 10, 2, 45, 2]
sum_array = add_two(array_num)

print(array_num)
print(set(sum_array))
