#!/usr/bin/env python
'''
Allows you to encrypt or decrypt text using the simple Caesar cipher.
'''

import argparse
import sys

def validate(dic):
    '''
    Validates the values of variables.

    The dictionary argument must be of the form
        `{(variable, `var_name`) : function}`,
    where the function is a validator returning true or false. This is useful
    for a large set of values to validate.
    '''
    for opt, is_valid in dic.iteritems():
        value, name = opt
        if not is_valid(value):
            sys.stderr.write('{0}: {1} is not valid for option {2}.'.format(
                'cipher.py', value, name))
            sys.exit(1)


def encrypt(key=0, text=None):
    '''
    Encrypts the text using the Caesarian cipher.
    '''
    text, modulus = text.lower(), ord('a') + 26
    rot = lambda x, k: chr(ord(x) + k % modulus)
    return ''.join(rot)


def decrypt(key=0, text=None):
    '''
    Decrypts the text using the Caesarian cipher.
    '''
    text, modulus = text.lower(), ord('a') + 26
    rot = lambda x, k: chr(ord(x) + k % modulus)
    return ''.join(rot)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog='cipher.py',
            description='cipher - simple text encryption',
            epilog='Please use RSA instead.')

    # Like tar, you must specify a direction
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--encrypt', action='store_true')
    group.add_argument('-d', '--decrypt', action='store_false')

    # The other options and arguments
    parser.add_argument(
        'text',
        help='The text to encrypt or decrypt.')
    parser.add_argument(
        'key',
        type=int,
        help='The numeric key to use (0 and 25, inclusive).')

    args = parser.parse_args().__dict__

#    # TODO: future support for other ciphers
#    parser.add_argument(
#        '-t',
#        '--type',
#        help='The type of encryption to use.'
#        choices=['Caesar'])
