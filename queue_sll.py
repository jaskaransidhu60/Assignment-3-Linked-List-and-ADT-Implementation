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
        self.front_node = None  # renamed to avoid conflict with 'front' method
        self.rear_node = None
        self._size = 0  # renamed to '_size' to ensure no method conflicts

    def enqueue(self, value):
        """Adds a new value to the end of the queue."""
        new_node = QueueNode(value)
        if self.rear_node is None:
            # If the queue is empty, the new node is both the front and rear
            self.front_node = new_node
        else:
            # Link the current rear to the new node
            self.rear_node.next = new_node
        self.rear_node = new_node
        self._size += 1

    def dequeue(self):
        """Removes and returns the value from the front of the queue."""
        if self.is_empty():
            raise QueueException("Dequeue from empty queue")
        value = self.front_node.value
        self.front_node = self.front_node.next
        if self.front_node is None:
            # Queue is empty after removal
            self.rear_node = None
        self._size -= 1
        return value

    def front(self):
        """Returns the value at the front without removing it."""
        if self.is_empty():
            raise QueueException("Front of empty queue")
        return self.front_node.value

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise."""
        return self._size == 0

    def size(self):
        """Returns the current size of the queue."""
        return self._size

    def __str__(self):
        """String representation for debugging."""
        result = "QUEUE ["
        current = self.front_node
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += " -> "
            current = current.next
        result += "]"
        return result
