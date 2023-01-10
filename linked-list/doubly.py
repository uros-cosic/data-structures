class Empty(Exception):
    """Error while attempting to access the element from an empty container"""
    pass

class DoublyList:
    """Doubly Linked List"""

    class _Node:
        """Lightweight, nonpublic Node class"""
        __slots__ = '_val', '_next', '_prev'

        def __init__(self, val, next, prev):
            self._val = val
            self._next = next
            self._prev = prev

    def __init__(self):
        """Create an empty doubly list"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in a doubly list"""
        return self._size

    def is_empty(self):
        """Return True if the doubly list is empty"""
        return self._size == 0

    def first(self):
        """Return the first element of a list
        
        Raise Empty if list is empty
        """
        if self.is_empty():
            raise Empty('List is empty')
        return self._head

    def last(self):
        """Return the last element of a list
        
        Raise Empty if list is empty
        """
        if self.is_empty():
            raise Empty('List is empty')
        return self._tail

    def append(self, e):
        """Add element e to the end of the list"""
        new = self._Node(e, None, self._tail)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1

    def pop(self):
        """Remove and return the last element of the list
        
        Raise Empty if the list is empty
        """
        if self.is_empty():
            raise Empty('List is empty')
        res = self._tail._val
        self._tail = self._tail._prev
        self._size -= 1
        if self.is_empty():
            self._head = None
        return res

    def insert_first(self, e):
        """Insert elemet e to the head of the list"""
        new = self._Node(e, self._head, None)
        self._head = new
        self._size += 1

    def remove_first(self):
        """Remove and return the first element of the list
        
        Raise Empty if the list is empty
        """
        if self.is_empty():
            raise Empty('List is empty')
        res = self._head._val
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return res

    def insert(self, node, e):
        """Insert element e after node"""
        new = self._Node(e, node._next, node)
        node._next._prev = new
        node._next = new
        self._size += 1
        