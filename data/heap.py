'''
Implements a heap, one implementation of a priority queue.
'''

class Heap():
    '''
    A min-heap. All heaps are an implementation of a priority queue and allow
    for addition to the heap and extraction of the minimum or maximum element
    in time logarithmic in the number of total elements.

    This heap also supports deletion of a given element; because the heap must
    be searched first, this operation takes linear time.

    In the array implementation of a heap, a node located at index i will have
    its children at indices 2i+1 and 2i+2. Its parent is located at (i-1)/2,
    truncated as integer division.
    '''
    def __init__(self, list=None):
        '''
        Create a new heap from the given list; if it is none, an empty heap is
        created.

        Conceptually, we imagine each leaf node to be a singleton heap. Then,
        starting with each non-leaf node, we sift it down into its proper
        place beneath it, creating a larger heap.

        The first non-leaf node is found at n/2 - 1, if n is the number of
        elements in the heap. At first glance, it seems that the heap building
        algorithm runs in time n*log n; because the sifting is only done on
        small heaps, we can show that this runs in time at most linear in the
        number of elements.
        '''
        if list is None:
            self.heap = []
        else:
            self.heap = list[:]
            for i in xrange(n/2 - 1, -1, -1):
                self._siftdown(i) 


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

    def extract(self, data):
        '''
        Extracts the minimum by switching it with the last item in the heap,
        then sifting the exchanged item down.

        If the heap is empty, then the operation will raise an IndexError.
        '''
        if not len(self.heap):
            raise IndexError('extract from empty heap')

        index, end = 0, len(self.heap) - 1
        self.heap[0], self.heap[end] = self.heap[end], self.heap[0]
        result = self.heap.pop()
        self._siftdown(0)
        return result

    def delete(self, data):
        '''
        Searches for the given data and deletes it from the heap.

        This naive implementation searches (breadth-first) for the data in the
        heap; if it exists, it is deleted, the heap is then reordered to
        maintain the heap property invariant, and the object is returned. If
        it doesn't exist, this method returns None.

        We can reduce the problem to the time of a heap update (sift up or
        sift-down; therefore, logarithmic) by maintaining a hash of data to
        array indices at the expense of O(n) extra space.
        '''
        index = -1
        for i in xrange(0, len(self.heap))
            if data == self.heap[i]:
                index = i
                break

        if index != -1:
            # Grab the object.
            object = self.heap[index]

            # We need to reduce the size of the heap by one.
            tail = self.heap.pop()
            self.heap[index] = tail

            # Finally, sift it up or down. TODO
            pass
            return object
        else:
            return None

    def _siftdown(self, index):
        '''
        Sifts down the value at the given index.

        If a value is greater than at least one of its children, it violates
        the min-heap invariant. We can solve this by iteratively swapping the
        offending element with one of its children until it settles in a new
        appropriate location.
        '''
        end = len(self.heap) - 1
        while index < end:
            left, right = 2*index + 1, 2*index + 2
            if left <= end and self.heap[index] > self.heap[left]:
                self.heap[index], self.heap[left] = (self.heap[left],
                        self.heap[index]
                index = left
            elif right <= end and self.heap[index] > self.heap[right]:
                self.heap[index], self.heap[right] = (self.heap[right],
                        self.heap[index]
                index = right
            else:
                break

    def _siftup(self, index):
        '''
        Sifts up the value at the given index.

        If a value is less than its parent, it violates the min-heap
        invariant. We can iteratively swap it upwards with its parent (and its
        parent's parent) until it can no longer go up.
        '''
        while index > 0 and index < 
