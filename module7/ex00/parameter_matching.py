#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print('none')
else:
    parameter = sys.argv[1]
    respond = input('What was the parameter? ')
    if (parameter == respond):
        print('Good job!')
    else:
        print('Nope, sorry...')