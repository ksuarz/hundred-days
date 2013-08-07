#!/usr/bin/env python
'''
Implements Dijkstra's shunting yard algorithm. It parses math statements in
infix notation and returns the equivalent statement in postfix notation.
'''

import argparse
import sys
from tokenizer import Tokenizer

class Shunter():
    '''
    Converts infix to postfix, storing tokens and the progress of the
    computation as object data.
    '''
    def __init__(self, **kwargs):
        '''
        Initialize the module.
        '''
        self.expr = ' '.join(expression)
        self.output = []
        self.operators = '+-*/^'
        self.tokenizer = Tokenizer(self.expr, '+-*/^()')

    def convert(self, expr):
       '''
       Converts the given infix into postfix.
       '''
       while self.tokenizer.has_token():
           token = self.tokenizer.next_token()
           if token.isdigit():
               self.output.append(token)
            elif token in self.operators:
                # TODO
                pass
        
    def eval(self, expr):
        '''
        Evaluates an expression in postfix notation.
        '''
        pass

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

        
