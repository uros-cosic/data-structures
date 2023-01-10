class Empty(Exception):
    """Error while attempting to access the element from an empty container"""
    pass

class SinglyList:
    """Singly Linked List"""

    class _Node:
        """Lightweight, nonpublic Node class"""
        __slots__ = '_val', '_next'
        
        def __init__(self, val, next):
            self._val = val
            self._next = next

    def __init__(self):
        """Create an empty linked list"""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in a linked list"""
        return self._size

    def is_empty(self):
        """Return True if the linked list is empty"""
        return self._size == 0

    def first(self):
        """Return the first element in a linked list
        
        Raise Empty if the list is empty
        """
        if self.is_empty():
            raise Empty('Linked List is empty')
        return self._head._val

    def last(self):
        """Return the last element in a linked list
        
        Raise Empty if the list is empty
        """
        if self.is_empty():
            raise Empty('Linked List is empty')
        curr = self._head
        while curr._next:
            curr = curr._next
        return curr._val

    def append(self, e):
        """Add element e to the end of the linked list"""
        new = self._Node(e, None)
        if self.is_empty():
            self._head = new
        else:
            curr = self._head
            while curr._next:
                curr = curr._next
            curr._next = new
        self._size += 1

    def pop(self):
        """Remove and return the last element of the linked list
        
        Raise Empty if the list is empty
        """
        if self.is_empty():
            raise Empty('Linked List is empty')
        curr, prev = self._head, None
        while curr._next:
            curr = curr._next
            prev = curr
        res = curr._val
        if prev:
            prev._next = None
        else:
            self._head = None
        self._size -= 1
        return res

    def insert_first(self, e):
        """Set element e as new head of the linked list"""
        new = self._Node(e, self._head)
        self._head = new
        self._size += 1

    def remove_first(self):
        """Remove and return head of the linked list
        
        Raise Empty if the linked list is empty
        """
        if self.is_empty():
            raise Empty('Linked List is empty')
        res = self._head._val
        self._head = self._head._next
        self._size -= 1
        return res

    def insert(self, node, e):
        """Insert element e after node"""
        new = self._Node(e, node._next)
        node._next = new
        self._size += 1
