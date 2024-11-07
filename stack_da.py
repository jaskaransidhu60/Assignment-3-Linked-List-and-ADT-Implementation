# Name: JASKARAN SINGH SIDHU
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 4 November
# Description: Implements a stack using a dynamic array, supporting push, pop, and top operations.

class DynamicArray:
    def __init__(self):
        self.array = [None] * 4
        self.size = 0
        self.capacity = 4

    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = value
        self.size += 1

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

class StackException(Exception):
    """Custom exception for Stack operations."""
    pass

class Stack:
    def __init__(self):
        self._da = DynamicArray()

    def push(self, value):
        self._da.append(value)

    def pop(self):
        if self.is_empty():
            raise StackException("Pop from empty stack")
        value = self._da.array[self._da.size - 1]
        self._da.size -= 1
        return value

    def top(self):
        if self.is_empty():
            raise StackException("Top of empty stack")
        return self._da.array[self._da.size - 1]

    def is_empty(self):
        return self._da.size == 0
