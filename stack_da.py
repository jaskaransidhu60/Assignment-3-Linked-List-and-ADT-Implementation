# Name: JASKARAN SINGH SIDHU
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 4 November
# Description: Implements a stack using a dynamic array, supporting push, pop, and top operations.

from dynamic_array import DynamicArray

class StackException(Exception):
    """Custom exception for Stack operations."""
    pass

class Stack:
    def __init__(self):
        self._da = DynamicArray()

    def push(self, value):
        self._da.append(value)

    def pop(self):
        if self._da.is_empty():
            raise StackException("Pop from empty stack")
        return self._da.pop()

    def top(self):
        if self._da.is_empty():
            raise StackException("Top of empty stack")
        return self._da.get_at_index(self._da.length() - 1)
