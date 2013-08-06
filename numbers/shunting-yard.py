#!/usr/bin/env python
'''
Implements Dijkstra's shunting yard algorithm. It parses math statements in
infix notation and returns the equivalent statement in postfix notation.
'''

import argparse
import sys

if __name__ == '__main__':
    # Set up command line options
    parser = argparse.ArgumentParser(
            prog='shunting-yard.py',
            description='shunting-yard - convert infix to postfix')
    parser.add_argument(
            'expression',
            dest='input',
            metavar='EXPR',
            help='The infix expression to convert.')
    parser.add_argument(
            '-e',
            '--evaluate',
            action='store_true',
            help='Evaluate the expression instead of converting it.')

    if len(sys.argv)
