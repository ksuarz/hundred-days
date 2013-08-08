#!/usr/bin/env python
'''
Reverses a string.
'''

import sys

if len(sys.argv) < 2:
    print 'Usage: reverse.py [TEXT]'
else:
    # Gather up the 'arguments' as one long string.
    text = ' '.join(sys.argv[1:])
    result = [x for x in reversed(text)]
    
    # If you prefer a more manual way:
    # result = [text[i] for i in reversed(range(0, len (text)))]
    
    print ''.join(result)
