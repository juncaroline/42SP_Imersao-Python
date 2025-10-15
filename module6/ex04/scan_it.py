#!/usr/bin/python3

import sys
import re

if len(sys.argv) != 3:
    print('none')
else:
    pattern = sys.argv[1]
    text = sys.argv[2]
    match = re.findall(pattern, text)
    if (len(match) == 0):
        print('none')
    else:
        print(len(match))
