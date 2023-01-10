class Empty(Exception):
    """Error while attempting to access the element from an empty container"""
    pass

class ListStack:
    """LIFO Stack Implementation using Python List"""
    def __init__(self):
        """Create an empty stack"""
        self._data = []

    def __len__(self):
        """Return the number of elements in a stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._data.append(e)

    def top(self):
        """Return the element at the top of the stack

        Raise Empty exception if stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove and return the top element of the stack
        
        Raise Empty if stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
        
    