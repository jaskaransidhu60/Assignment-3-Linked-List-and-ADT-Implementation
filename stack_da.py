# Name: JASKARAN SINGH SIDHU
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 4 November
# Description: Implements a Stack using a DynamicArray as the underlying structure,
# providing push, pop, and top operations.


class StackException(Exception):
    """Custom exception to be used by Stack class."""
    pass

class Stack:
    def __init__(self):
        """Initialize new stack based on Dynamic Array."""
        self._da = DynamicArray()

    def __str__(self) -> str:
        """Return content of stack in human-readable form."""
        out = "STACK: " + str(self.size()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """Return True if the stack is empty, False otherwise."""
        return self._da.is_empty()

    def size(self) -> int:
        """Return the number of elements currently in the stack."""
        return self._da.length()

    # -----------------------------------------------------------------------
    def push(self, value: object) -> None:
        """Add a new element to the top of the stack."""
        self._da.append(value)

    def pop(self) -> object:
        """Remove and return the top element of the stack. Raise exception if empty."""
        if self.is_empty():
            raise StackException("Cannot pop from an empty stack")
        top_value = self._da[self.size() - 1]
        self._da.remove_at_index(self.size() - 1)
        return top_value

    def top(self) -> object:
        """Return the top element of the stack without removing it. Raise exception if empty."""
        if self.is_empty():
            raise StackException("Cannot access top of an empty stack")
        return self._da[self.size() - 1]
