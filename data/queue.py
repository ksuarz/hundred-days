'''
A simple implementation of a queue that permits constant-time enqueue and
dequeue operations.
'''

class Node():
    '''
    A doubly-linked node with pointers to both the next and previous nodes.

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
    A simple first-in, first-out queue. It is implemented as a doubly-linked
    list, to allow for constant-time enqueue and dequeue operations.
    '''
    def __init__(self):
        '''
        Creates an empty queue.
        '''
        self.head, self.tail = None, None
        self.size = 0

    def enqueue(self, obj):
        '''
        Adds the given object to the queue.
        '''
        if not size:
            self.head = self.tail = Node(data=obj)
        else:
            node = Node(data=obj, next=self.tail)
            self.tail.prev = node
            self.tail = node
            self.size += 1

    def dequeue(self):
        '''
        Removes the next object from the queue. If the queue is empty, an
        IndexError is raised.
        '''
        if not size:
            raise IndexError('dequeue from empty queue')
        elif size == 1:
            data = self.head.data
            self.head, self.tail = None, None
        else:
            data = self.head.data
            self.head = self.head.prev
        size -= 1
        return data
