# Name: JASKARAN SINGH SIDHU
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 4 November
# Description: Implements a queue using a static array, supporting enqueue, dequeue, and front operations.

from static_array import StaticArray

class QueueException(Exception):
    """Custom exception for Queue operations."""
    pass

class Queue:
    def __init__(self, capacity=4):
        self._sa = StaticArray(capacity)
        self._front = 0
        self._rear = 0
        self._size = 0

    def enqueue(self, value):
        if self._size == self._sa.length():
            self._resize(2 * self._sa.length())
        self._sa[self._rear] = value
        self._rear = (self._rear + 1) % self._sa.length()
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise QueueException("Dequeue from empty queue")
        value = self._sa[self._front]
        self._front = (self._front + 1) % self._sa.length()
        self._size -= 1
        return value

    def front(self):
        if self._size == 0:
            raise QueueException("Front of empty queue")
        return self._sa[self._front]

    def _resize(self, new_capacity):
        new_sa = StaticArray(new_capacity)
        for i in range(self._size):
            new_sa[i] = self._sa[(self._front + i) % self._sa.length()]
        self._sa = new_sa
        self._front = 0
        self._rear = self._size
