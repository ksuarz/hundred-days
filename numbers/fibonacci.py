#!/usr/bin/env python
'''
Calculates the Fibonacci sequence to an arbitrary number of digits.
'''

import sys

if not sys.argv or len(sys.argv) != 2:
    print 'Usage: fibonacci.py N (where N is a positive number)'
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print 'fibonacci.py: That\'s not a valid integer.'
    sys.exit(1)

if n < 0:
    print 'fibonacci.py: Must be a positive number.'
    sys.exit(1)

def fibgen(n):
    '''
    A generator, because that's what the cool kids do.
    '''
    x, y, z = 0, 1, 0
    while z < n:
        x, y = y, x + y
        z += 1
        yield x

for num in fibgen(n):
    print num
