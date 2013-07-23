'''
Checks if a given word or sentence is a palindrome. Whitespace is ignored
for the purposes of this program.
'''

import sys

if len(sys.argv) < 2:
    print 'Usage: palindrome.py [TEXT]'
else:
    # Get the 'sentence' to analyze.
    whitespace = ' \t\n'
    text = ' '.join(sys.argv[1:]).lower()
    string = ''.join([c.lower() for c in text if c not in whitespace])

    # O(n) check with n/2 comparisons
    end = len(string)
    for i in range(0, end/2 + 1):
        if string[i] != string[end - i - 1]:
            print 'Not a palindrome.'
            break
    else:
        print 'It\'s a palindrome!'
