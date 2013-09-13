'''
An implementation of a circular linked list.
'''

class Node():
    '''
    A basic node class.
    '''
    def __init__(self, data=None, next=None):
        '''
        Creates a new node.
        '''
        self.data = data
        self.next = next

class CircularLinkedList():
    '''
    A circular linked list, where we have constant-time access to both the
    first and last contained elements.
    '''
    def __init__(self):
        '''
        Creates an empty list.
        '''
        self.tail = None
        self.size = 0

    def append(self, obj):
        '''
        Adds the given item to the end of the list.
        '''
        node = Node(data=obj)
        if not self.size:
            self.tail = node
            self.tail.next = self.tail
        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, obj):
        '''
        Adds the given item to the front of the list.
        '''
        node = Node(data=obj)
        if not self.size:
            self.tail = node
            self.tail.next = self.tail
        else:
            node.next = self.tail.next
            self.tail.next = node
        self.size += 1

    def get(self, index):
        '''
        Returns the item at the given index.
        '''
        if self.size == 0 or index < 0 or index >= self.size:
            raise IndexError('Linked list index out of range')
        else:
            ptr = self.tail.next
            for i in range(0, index):
                ptr = ptr.next
            return ptr.data

    def remove(self, index):
        '''
        Removes the object at the given position from the list and returns it.
        '''
        if self.size == 0 or index < 0 or index >= self.size:
            raise IndexError('Linked list index out of range')
        else:
            prev, curr = self.tail, self.tail.next
            for i in range(0, index):
                prev, curr = curr, curr.next
            prev.next = curr.next
            if index == self.size - 1:
                self.tail = prev
            self.size -= 1
            return curr.data

    def print(self):
        '''
        Returns the linked list as a vanilla Python list.
        '''
        if self.size == 0:
            return []
        else:
            result, ptr = [], self.tail.next
            for i in range(0, self.size):
                result.append(ptr.data)
                ptr = ptr.next
            return result
