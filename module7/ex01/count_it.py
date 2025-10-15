#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
    print('none')
else:
    print ('parameters:', len(sys.argv) - 1)
    for arg in sys.argv[1:]:
        print(f'{arg}: {len(arg)}')