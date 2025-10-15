#!/usr/bin/python3

import sys

def downcase_it(s):
    return s.lower()

if len(sys.argv) < 2:
    print('none')
else:
    i = 1
    while i < len(sys.argv):
        print(downcase_it(sys.argv[i]))
        i += 1