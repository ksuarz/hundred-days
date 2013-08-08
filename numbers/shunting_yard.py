#!/usr/bin/env python
'''
Implements Dijkstra's shunting yard algorithm. It parses math statements in
infix notation and returns the equivalent statement in postfix notation.

The input string is scanned once, from start to end; thus this algorithm runs
in linear time.

Here is the algorithm in pseudocode:
    stack <- Stack()
    output <- Queue()
    for each token in input:
        if token is number:
            enqueue token to output
        else if token is operator:
            top <- stack.peek()
            if top is number:
                # It must be an operator.
                parser error
            while top.precedence > token.precedence:
                output.enqueue(stack.pop())
            stack.push(token)
        else:
            parser error
'''

import argparse
import sys
from tokenizer import Tokenizer

class Shunter():
    '''
    Converts infix to postfix, storing tokens and the progress of the
    computation as object data.
    '''
    def __init__(self, expression, **kwargs):
        '''
        Initialize the module.
        '''
        self.expr = ' '.join(expression)
        self.output = []
        self.operators = {
            '+': lambda x,y: x + y,
            '-': lambda x,y: x - y,
            '/': lambda x,y: x / y,
            '*': lambda x,y: x * y,
            '^': lambda x,y: x ** y
        }
        self.tokenizer = Tokenizer(self.expr, '+-*/^')
        self.precedence = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2 }

    def _has_higher_precedence(self, op1, op2):
        '''
        Returns true if op1 has a higher precedence than op2; false otherwise.
        '''
        return self.precedence[op1] > self.precedence[op2]

    def convert(self):
        '''
        Converts the given infix into postfix using the shunting-yard
        algorithm.
        '''
        stack = []
        while self.tokenizer.has_token():
            token = self.tokenizer.next_token().strip()
            if token.isdigit():
                self.output.append(token)
            elif self.operators.has_key(token):
# TODO optimize
                if len(stack) == 0:
                    stack.append(token)
                else:
                    while len(stack) and self._has_higher_precedence(
                            stack[-1], token):
                        self.output.append(stack.pop())
                    stack.append(token)
            else:
                print 'Parser error: invalid character "{0}"'.format(token)
                sys.exit(1)
        while len(stack):
            print stack
            self.output.append(stack.pop())
        return ' '.join(self.output)
        
    def eval(self):
        '''
        Evaluates an expression in postfix notation.
        '''
        stack = []
        for token in self.output:
            if token.isdigit():
                stack.append(token)
            elif self.operators.has_key(token):
                try:
                    y, x = stack.pop(), stack.pop()
                    stack.append(self.operators[token](x, y))
                except IndexError:
                    print 'Evaluator error: invalid postfix. Sorry.'
                    sys.exit(1)
        else:
            if len(stack) != 1:
                print 'Invalid postfix.'
                sys.exit(1)
            else:
                return stack.pop()

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

        
