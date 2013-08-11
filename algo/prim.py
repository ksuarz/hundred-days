#!/usr/bin/env python
'''
An implementation of the Prim-Jarnik algorithm, a greedy method of finding
the minimum spanning tree for a connected, weighted, undirectred graph.
'''

class Heap():
    '''
    A custom min-heap that permits logarithmic-time deletions of a given
    key value in the heap (at the cost of linear extra space).

    In the array implementation of a heap, a node located at index i will have
    its children at indices 2i+1 and 2i+2. Its parent is located at (i-1)/2,
    truncated as integer division.
    '''
    def __init__(self):
        '''
        Create a new empty heap.
        '''
        self.heap = []

    def insert(self, data):
        '''
        Inserts the data by adding it to the bottom of the heap, then sifting
        it up to its proper place.
        '''
        self.heap.append(data)
        index = len(self.heap) - 1
        parent = (index-1) / 2

        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = (self.heap[parent],
                    self.heap[index])
            index, parent = parent, (index-1) / 2

    def delete(self, data):
        '''
        
        '''

    def extract(self, data):
        '''
        Extracts the minimum by switching it with the last item in the heap,
        then sifting the exchanged item down.
        '''
        index, end = 0, len(self.heap) - 1
        self.heap[0], self.heap[end] = self.heap[end], self.heap[0]

        while index > end:
            left, right = 2*index + 1, 2*index + 2
            if self.heap[index] > self.heap[left]:
                self.heap
            elif self.heap[index] > self.heap[right]:
                pass
            else:
                break
        
        

# Elements in the heap will hold the vertices we have yet to span (V-X) - the horizon or fringe
# For each v in V-X, key[v] = cheapest edge (u, v) with u in X; if there does not exist u,
#   then key[v] = +infinity

# After moving a vertex from V-X to X, the key values of other vertices change.
# We must now update the key values for all vertices adjacent to the pulled in one
def update():
    when v added to X:
        for each (v, w) in E:
            if w in V-X:
                delete w from heap
                recompute key[w] = min(key[w], c[v, w])
                re-insert w into heap
