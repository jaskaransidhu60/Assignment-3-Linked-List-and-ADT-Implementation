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

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if not self.top_node:
            raise StackException("Pop from empty stack")
        value = self.top_node.value
        self.top_node = self.top_node.next
        return value

    def top(self):
        if not self.top_node:
            raise StackException("Top of empty stack")
        return self.top_node.value
