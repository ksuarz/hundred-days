#!/usr/bin/python
'''
Converts words to pig latin. This is a very naive implementation. All
non-alphanumeric, non-whitespace characters are treated as part of a word.
'''

import sys

if len(sys.argv) < 2:
    print 'Usage: piglatin.py [TEXT]'
else:
    # First, build up our vowels and consonants
    start, end = ord('a'), ord('z') + 1
    vowels = 'aeiou'
    consonants = [chr(i) for i in range(start, end) if chr(i) not in vowels]

    # Now, do some text manipulation
    text = ' '.join(sys.argv[1:]).lower().strip()
    result = []
    for word in text.split():
        c = word[0]
        if c in consonants:
            result.append(word[1:] + '-' + c + 'ay')
        elif c in vowels:
            result.append(word + 'way')
        else:
            result.append(word)

    print ' '.join(result)
