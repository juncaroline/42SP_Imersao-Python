#!/usr/bin/python3

import sys

def shrink(arg):
    return arg[:8]

def enlarge(arg):
    return arg + 'Z' * (8 - len(arg))

arguments = sys.argv[1:]
i = 0

if len(sys.argv) < 2:
    print('none')
while i < len(arguments):
    arg = arguments[i]
    if len(arg) > 8:
        print(shrink(arg))
    elif len(arg) < 8:
        print(enlarge(arg))
    else:
        print(arg)
    i += 1