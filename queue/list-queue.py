class Empty(Exception):
    """Error while attempting to get an element from a empty queue"""
    pass

class ListQueue:
    """FIFO Queue Implementation Using Python List"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in a queue"""
        return len(self._data)
    
    def is_empty(self):
        """Return True if the queue is empty"""
        return len(self._data) == 0

    def first(self):
        """Return the element at the front of the queue
        
        Raise Empty if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element in queue
        
        Raise Empty if queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        res = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return res

    def enqueue(self, e):
        """Add element e to the back of the queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, c):
        """Resize the queue to capacity c"""
        old = self._data
        self._data = [None] * c
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0