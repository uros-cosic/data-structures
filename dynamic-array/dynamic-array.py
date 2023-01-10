import ctypes

class DynamicArray:
    """A dynamic array class similar to python list"""
    def __init__(self):
        """Create an empty array"""
        self._n = 0                                     # Elements count
        self._capacity = 1                              # Initial capacity
        self._A = self._create_array(self._capacity)    # Low-level array

    def __len__(self):
        """Return the number of stored elements in the array"""
        return self._n

    def __getitem__(self, k):
        """Return the element at index k"""
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')
        return self._A[k]

    def append(self, obj):
        """Add object to the end of an dynamic array"""
        if self._n == self._capacity:           # Array is full
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c"""
        B = self._create_array(c)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = c

    def _create_array(self, c):
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()
        
    