#!/usr/bin/python3

import sys
import re

if len(sys.argv) != 2:
    print('none')
else:
    pattern = r'z'
    text = sys.argv[1]
    match = re.findall(pattern, text)
    output = ''.join(match)
    if (len(match) == 0):
        print('none')
    else:
        print(output)