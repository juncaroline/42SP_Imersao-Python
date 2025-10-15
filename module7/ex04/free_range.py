#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
    print('none')
else:
    x = range(int(sys.argv[1]) - 1, int(sys.argv[2]) + 1)
    result = []
    i = 1
    while (i < len(x)):
        result.append(x[i])
        i += 1
    print(result)