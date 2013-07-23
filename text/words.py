'''
Counts the number of words in a given sentence. For our purposes, a 'word' is
any sequence of non-whitespace characters.
'''

import sys

if len(sys.argv) < 2:
    print 'Usage: words.py [TEXT]'
else:
    # Gotta join them in case someone uses quotes
    text = ' '.join(sys.argv[1:]).lower().strip()
    print 'Number of words: {0}'.format(len(text.split()))
