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
        self.top_node = None
        self.size = 0  # Added size attribute to track stack size

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top_node
        self.top_node = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise StackException("Pop from empty stack")
        value = self.top_node.value
        self.top_node = self.top_node.next
        self.size -= 1
        return value

    def top(self):
        if self.is_empty():
            raise StackException("Top of empty stack")
        return self.top_node.value

    def is_empty(self):
        return self.size == 0
