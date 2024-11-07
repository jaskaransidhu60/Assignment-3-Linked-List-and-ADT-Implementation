# Name: JASKARAN SINGH SIDHU
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 4 November
# Description: Implements a queue using a static array with circular buffer logic,
# supporting enqueue, dequeue, and front operations with proper resizing.

from static_array import StaticArray

class QueueException(Exception):
    """Custom exception to be used by Queue class."""
    pass

class Queue:
    def __init__(self) -> None:
        """Initialize a new queue based on Static Array with a default capacity of 4."""
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self) -> str:
        """Override string method to provide more readable output."""
        size = self.size()
        out = "QUEUE: " + str(size) + " element(s). ["
        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa[front_index]) + ', '
            front_index = self._increment(front_index)
        if size > 0:
            out += str(self._sa[front_index])
        return out + ']'

    def is_empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        return self._current_size == 0

    def size(self) -> int:
        """Return the number of elements currently in the queue."""
        return self._current_size

    def _increment(self, index: int) -> int:
        """Move index to next position, wrapping around if needed."""
        return (index + 1) % self._sa.length()

    def enqueue(self, value: object) -> None:
        """Add a new value to the end of the queue, resizing if needed."""
        if self.size() == self._sa.length():
            self._double_queue()

        self._back = self._increment(self._back)
        self._sa[self._back] = value
        self._current_size += 1

    def dequeue(self) -> object:
        """Remove and return the value from the front of the queue."""
        if self.is_empty():
            raise QueueException("Cannot dequeue from an empty queue")

        value = self._sa[self._front]
        self._sa[self._front] = None  # Clear out the value for better debugging
        self._front = self._increment(self._front)
        self._current_size -= 1
        return value

    def front(self) -> object:
        """Return the value at the front of the queue without removing it."""
        if self.is_empty():
            raise QueueException("Cannot access front of an empty queue")
        return self._sa[self._front]

    def _double_queue(self) -> None:
        """Double the capacity of the queue when it is full."""
        new_capacity = self._sa.length() * 2
        new_sa = StaticArray(new_capacity)

        # Copy elements in order starting from _front
        index = self._front
        for i in range(self._current_size):
            new_sa[i] = self._sa[index]
            index = self._increment(index)

        # Update to the new array and reset front and back positions
        self._sa = new_sa
        self._front = 0
        self._back = self._current_size - 1
