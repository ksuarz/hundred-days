'''
A simple implementation of a queue that permits constant-time enqueue and
dequeue operations.
'''

class Node():
    '''
    A doubly-linked node with next and previous pointers.

    The queue uses these nodes like a linked list to maintain its required
    structure.
    '''
    def __init__(self, data=None, next=None, prev=None):
        '''
        Creates a new node.
        '''
        self.data = data
        self.next, self.prev = next, prev

class Queue():
    '''
    A simple first-in, first-out queue. It is implemented as a circular,
    doubly-linked list to allow for constant-time enqueue and dequeue
    operations.
    '''
    def __init__(self):
        '''
        Creates an empty queue.
        '''
        self.tail = None
        self.size = 0

    def enqueue(self, obj):
        '''
        Adds the given object to the queue.
        '''
        node = Node(data=obj)
        if not self.size:
            # Special case for adding the first item
            self.tail = node
            self.tail.next, self.tail.prev = node, node
        else:
            # `node` is now the new end; `node.next` should be the front
            node.next, node.prev = self.tail.next, self.tail.prev
            self.tail.prev.next, self.tail.next.prev = node, node
            self.tail = node
        self.size += 1

    def dequeue(self):
        '''
        Removes the next object from the queue. If the queue is empty, an
        IndexError is raised.
        '''
        if not self.size:
            raise IndexError('dequeue from empty queue')
        elif self.size == 1:
            data = self.tail.data
            self.tail = None
        else:
            # `self.tail.prev.next` should now point to the front of the queue
            data = self.tail.data
            self.tail.prev.next = self.tail.next
            self.tail.next.prev = self.tail.prev
            self.tail = self.tail.prev
        self.size -= 1
        return data
