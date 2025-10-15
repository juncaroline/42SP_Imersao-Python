#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
    print('none')
else:
    i = 1
    while (i < len(sys.argv)):
        arg = sys.argv[i]
        if not arg.endswith('ism'):
            print(arg + 'ism')
        i += 1