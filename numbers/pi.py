'''
Given a number n, finds pi to the nth digit. I'm going to use Leibniz's
formula for pi, which is

        pi/4 = sum[k=1..] ((-1)^(k-1))/(2k-1)
             = 1 - 1/3 + 1/5 - 1/7 + ...
'''

import sys

if len(sys.argv) != 2:
    print 'Usage: pi.py [NUMBER]'
else:
    try:
        n = int(sys.argv[1])
    except ValueError:
        print 'That\'s not a valid number.'
        sys.exit(1)

    max = 200
    if n > max:
        n = max
        print 'That\'s a lot of digits. Let\'s stop at {0} places.'.format(max)
