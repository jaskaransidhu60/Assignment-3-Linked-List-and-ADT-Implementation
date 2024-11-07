# Name: JASKARAN SINGH SIDHU
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 4 November
# Description: Implements a Singly Linked List with methods to insert, remove, count, find, and slice elements.
# This structure uses a front sentinel node for easier head management and supports a range of list operations with O(N) efficiency where necessary.

class SLLException(Exception):
    """Custom exception for Singly Linked List errors"""
    pass

class SLNode:
    def __init__(self, value: object):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = SLNode(None)  # sentinel node
        self._size = 0
    
    def insert_front(self, value: object) -> None:
        # Implementation of insert_front
        pass
    
    def insert_back(self, value: object) -> None:
        # Implementation of insert_back
        pass

    # Implement additional LinkedList methods based on requirements
