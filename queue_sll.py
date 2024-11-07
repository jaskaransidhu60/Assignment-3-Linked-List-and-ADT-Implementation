# Name: JASKARAN SINGH SIDHU
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 4 November
# Description: Implements a queue using a singly linked list, supporting enqueue, dequeue, and front operations.

class QueueException(Exception):
    """Custom exception for Queue operations."""
    pass

class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def enqueue(self, value):
        new_node = QueueNode(value)
        if not self.rear_node:
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node

    def dequeue(self):
        if not self.front_node:
            raise QueueException("Dequeue from empty queue")
        value = self.front_node.value
        self.front_node = self.front_node.next
        if not self.front_node:
            self.rear_node = None
        return value

    def front(self):
        if not self.front_node:
            raise QueueException("Front of empty queue")
        return self.front_node.value
