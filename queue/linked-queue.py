class Empty(Exception):
    """Error while attempting to get an element from a empty queue"""
    pass

class LinkedQueue:
    """FIFO Queue Implementation Using Linked List"""
    class _Node:
        """Lightweight, nonpublic Node class"""
        __slots__ = '_val', '_next'

        def __init__(self, val, next):
            self._val = val
            self._next = next

    def __init__(self):
        """Create an empty Queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in a queue"""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        """Return the first element of the queue
        
        Raise Empty if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._val

    def dequeue(self):
        """Remove and return the first element in the queue
        
        Raise Empty if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        res = self._head._val
        self._head = self.head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return res

    def enqueue(self, e):
        """Add the element e to the end of the queue"""
        new = self._Node(e, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1