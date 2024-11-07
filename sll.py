# Name: JASKARAN SINGH SIDHU
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 4 November
# Description: Implements a Singly Linked List with methods for inserting, removing, counting, finding, and slicing nodes.

class SLLException(Exception):
    """Custom exception for Singly Linked List errors."""
    pass

class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = SLNode(None)  # sentinel node for simpler head operations
        self._size = 0

    def insert_front(self, value):
        """Insert node at the beginning of the list after the sentinel."""
        new_node = SLNode(value)
        new_node.next = self._head.next
        self._head.next = new_node
        self._size += 1

    def insert_back(self, value):
        """Insert node at the end of the list."""
        new_node = SLNode(value)
        current = self._head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self._size += 1

    def insert_at_index(self, index, value):
        """Insert node at a specific index."""
        if index < 0 or index > self._size:
            raise SLLException("Index out of bounds")
        new_node = SLNode(value)
        current = self._head
        for _ in range(index):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def remove_at_index(self, index):
        """Remove node at a specific index."""
        if index < 0 or index >= self._size:
            raise SLLException("Index out of bounds")
        prev = self._head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self._size -= 1

    def remove(self, value):
        """Remove first occurrence of the specified value."""
        current = self._head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False

    def count(self, value):
        """Count occurrences of the specified value in the list."""
        count = 0
        current = self._head.next
        while current is not None:
            if current.value == value:
                count += 1
            current = current.next
        return count

    def find(self, value):
        """Check if the specified value exists in the list."""
        current = self._head.next
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def slice(self, start_index, size):
        """Return a new LinkedList containing a slice of nodes from start_index with the given size."""
        if start_index < 0 or size < 0 or start_index + size > self._size:
            raise SLLException("Invalid slice parameters")
        sliced_list = LinkedList()
        current = self._head.next
        for _ in range(start_index):
            current = current.next
        for _ in range(size):
            sliced_list.insert_back(current.value)
            current = current.next
        return sliced_list

    def __str__(self):
        """Return a string representation of the list."""
        out = []
        current = self._head.next
        while current is not None:
            out.append(str(current.value))
            current = current.next
        return "SLL [" + " -> ".join(out) + "]"
