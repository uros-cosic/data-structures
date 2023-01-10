class Empty(Exception):
    """Error while attempting to access the element from an empty container"""
    pass

class LinkedStack:
    """LIFO Stack Implementation Using Linked List"""
    class _Node:
        """Lightweight, nonpublic Node class"""
        __slots__ = '_val', '_next'

        def __init__(self, val, next):
            self._val = val
            self._next = next

    def __init__(self):
        """Create an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in a stack"""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return the element at the top of the stack
        
        Raise Empty if stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._val

    def pop(self):
        """Remove and return the element at the top of the stack
        
        Raise Empty if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        res = self._head._val
        self._head = self._head._next
        self._size -= 1
        return res
