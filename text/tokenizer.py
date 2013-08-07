#!/usr/bin/env python
'''
Implements a simple string tokenizer, similar to the Java implementation in
java.util.StringTokenizer.
'''

class Tokenizer():
    '''
    Tokenizes strings like string.split(), but also returns the delimeters.
    '''
    def __init__(self, expression, delimeters):
        '''
        Sets up the tokenizer for use.

        `expression` - The expression to tokenize.
        `delimeters` - A string whose characters are the delimiting tokens.

        If no delimeter is specified, all whitespace (that is, tabs, spaces,
        and newlines) will be counted as a delimeter.
        '''
        self.expr = expression
        self.delims = delimeters

    def is_delimeter(self, char):
        '''
        Returns true if the given character is a delimeter; false if it is not
        or if you specify a string of length greater than one.
        '''
        return char in self.delims

    def has_token(self):
        '''
        Returns true if there is another token in the expression; false
        otherwise.
        '''
        return self._next_delim() != None

    def next_token(self):
        '''
        Returns the next token, or None if the end of the expression has
        been reached.

        Note that this class treats delimeters as tokens and will return them
        every other call to next_token.
        '''
        index = self._next_delim()
        if index is None:
            return None
        else:
            if index == 0:
                token = self.expr[0]
                self.expr = self.expr[1:]
            else:
                token = self.expr[:index]
                self.expr = self.expr[index:]
            return token
            
    def _next_delim(self):
        '''
        Scans the string for the next delimeter.
        '''
        if len(self.expr) == 0:
            return None
        else:
            for i in xrange(len(self.expr)):
                if self.expr[i] in self.delims:
                    return i
            return len(self.expr)
