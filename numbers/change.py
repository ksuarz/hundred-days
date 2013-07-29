#!/usr/bin/env python
'''
Makes change for you.
'''

import sys

if len(sys.argv) != 3:
    sys.stderr.write('Usage: change.py [cost] [amount-paid]\n')
else:
    try:
        cost, paid = float(sys.argv[1]), floag(sys.argv[2])
    except ValueError:
        sys.stderr.write('change.py: cost and amount paid must be floats')
        sys.exit(1)

    # TODO account for the strangeness involving floating point
    target = cost - paid
    if target < 0:
        print 'Not paid enough.'
        sys.exit(1)

    amounts = [100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
    change = []
    while target != 0:
    for amt in amounts:
        x = paid / 
        change.append()
        
