# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 4 November
# Description: Implementation of a Singly Linked List (SLL) with essential methods such as insert, remove, count, find, and slice.

class SLLException(Exception):
    """Custom exception for singly linked list errors."""
    pass

class SLNode:
    def __init__(self, value: object):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes an empty linked list with a front sentinel node.
        If start_list is provided, populate the linked list with its elements.
        """
        self._head = SLNode(None)  # sentinel node
        self._size = 0

        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def length(self) -> int:
        """Returns the number of elements in the linked list."""
        return self._size

    def insert_front(self, value: object) -> None:
        """Inserts a new node with the specified value at the front of the list."""
        new_node = SLNode(value)
        new_node.next = self._head.next
        self._head.next = new_node
        self._size += 1

    def insert_back(self, value: object) -> None:
        """Inserts a new node with the specified value at the back of the list."""
        new_node = SLNode(value)
        current = self._head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """Inserts a new node with the specified value at the given index."""
        if index < 0 or index > self._size:
            raise SLLException("Index out of bounds")
        
        new_node = SLNode(value)
        current = self._head
        for _ in range(index):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """Removes the node at the specified index."""
        if index < 0 or index >= self._size:
            raise SLLException("Index out of bounds")
        
        current = self._head
        for _ in range(index):
            current = current.next
        current.next = current.next.next
        self._size -= 1

    def remove(self, value: object) -> bool:
        """Removes the first occurrence of the specified value in the list."""
        current = self._head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False

    def count(self, value: object) -> int:
        """Counts the number of occurrences of the specified value in the list."""
        count = 0
        current = self._head.next
        while current is not None:
            if current.value == value:
                count += 1
            current = current.next
        return count

    def find(self, value: object) -> bool:
        """Checks if the specified value exists in the list."""
        current = self._head.next
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def slice(self, start_index: int, size: int) -> 'LinkedList':
        """
        Returns a new LinkedList containing a sublist from the given start index of the specified size.
        """
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

    def __str__(self) -> str:
        """Returns a string representation of the linked list."""
        output = []
        current = self._head.next
        while current is not None:
            output.append(str(current.value))
            current = current.next
        return "SLL [" + " -> ".join(output) + "]"


