#!/usr/bin/env python
'''
A simple implementation of a binary search tree. It supports all of the basic
operations - search, add, and delete. With the naive implementation, the tree
can degenerate to a linked list, and thus runs in linear time in the worst
case for searching.

To implement the comparison function, a function can be passed into the
constructor to define custom behavior. If none is specified a simple
comparison is used that relies on the default behavior of python objects.
'''

class BinaryNode():
    '''
    Implements a basic binary node with two children.
    '''
    def __init__(self, data=None, left=None, right=None):
        '''
        Constructs a new node.
        '''
        self.data = data
        self.left, self.right = left, right

    def isempty(self):
        '''
        Returns true if the node is empty; false otherwise.
        '''
        return self.data is None

class BinarySearchTree():
    def __init__(self, comparator=None):
        '''
        Constructs an empty tree.
        '''
        self.root = None
        if comparator is None:
            self.compare = lambda x,y: 1 if x > y else -1 if x < y else 0
        else:
            self.compare = comparator

    def add(self, obj):
        '''
        Adds the object to the tree if it doesn't already exist.

        If the data already exists in the tree, nothing is done. On average,
        it runs in time logarithmic in the number of nodes; in the worst case,
        it runs in linear time.
        '''
        if not self.root:
            self.root = BinaryNode(data=obj)
        else:
            ptr, target  = self.root, self.root
            while target is not None:
                result = self.compare(obj, ptr.data)
                if result < 0:
                    target = ptr.left
                elif result > 0:
                    target = ptr.right
                else:
                    # It already exists in the tree.
                    return
            target = BinaryNode(data=obj) 
