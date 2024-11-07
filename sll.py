# Name: JASKARAN SINGH SIDHU
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 4 November
# Description: Implementation of a singly linked list with methods like insert, remove, count, find, and slice.

class SLLException(Exception):
    """Custom exception to be used by Singly Linked List."""
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_index(self, index, value):
        if index < 0:
            raise SLLException("Index out of bounds")
        if index == 0:
            self.insert_front(value)
            return
        new_node = Node(value)
        current = self.head
        for i in range(index - 1):
            if not current:
                raise SLLException("Index out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def remove_at_index(self, index):
        if index < 0 or not self.head:
            raise SLLException("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            if not current.next:
                raise SLLException("Index out of bounds")
            current = current.next
        if not current.next:
            raise SLLException("Index out of bounds")
        current.next = current.next.next

    def count(self, value):
        count = 0
        current = self.head
        while current:
            if current.value == value:
                count += 1
            current = current.next
        return count

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def slice(self, start_index, size):
        if start_index < 0 or size < 0:
            raise SLLException("Invalid slice parameters")
        sliced_list = LinkedList()
        current = self.head
        for i in range(start_index):
            if not current:
                raise SLLException("Index out of bounds")
            current = current.next
        for i in range(size):
            if not current:
                raise SLLException("Insufficient elements for slicing")
            sliced_list.insert_back(current.value)
            current = current.next
        return sliced_list
