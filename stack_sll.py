# Name: JASKARAN SINGH SIDHU
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 4 November
# Description: Implements a stack using a singly linked list, supporting push, pop, and top operations.

class StackException(Exception):
    """Custom exception for Stack operations."""
    pass

class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None  # renamed to avoid conflict with method 'top'
        self._size = 0        # renamed to '_size' to avoid conflict with size attribute

    def push(self, value):
        """Adds a new value to the top of the stack."""
        new_node = StackNode(value)
        new_node.next = self.top_node
        self.top_node = new_node
        self._size += 1

    def pop(self):
        """Removes and returns the value from the top of the stack."""
        if self.is_empty():
            raise StackException("Pop from empty stack")
        value = self.top_node.value
        self.top_node = self.top_node.next
        self._size -= 1
        return value

    def top(self):
        """Returns the top value without removing it from the stack."""
        if self.is_empty():
            raise StackException("Top of empty stack")
        return self.top_node.value

    def is_empty(self):
        """Returns True if the stack is empty, False otherwise."""
        return self._size == 0

    def size(self):
        """Returns the current size of the stack."""
        return self._size
