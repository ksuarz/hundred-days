#!/usr/bin/env python
'''
Counts the number of vowels in a string.
'''

import sys

if len(sys.argv) < 2:
    print 'Usage: vowels.py [TEXT]'
else:
    text, vowels = ''.join(sys.argv[1:]).lower(), 'aeiou'
    count = 0

    for c in text:
        if c in vowels:
            count += 1

    print 'Number of vowels: {0}'.format(count)
