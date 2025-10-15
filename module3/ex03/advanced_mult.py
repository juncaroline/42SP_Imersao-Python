#!/usr/bin/python3

i = 0
x = 0

while (x <= 10):
    print(f"Table of {x}: ", end=" ")
    while (i <= 10):
        print(i * x, end=" ")
        i += 1
    x += 1
    i = 0
    print()