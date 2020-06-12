class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next_node = next

    def get_value(self):
        # returns the node's data 
        return self.value

    def get_next(self):
        # returns the thing pointed at by this node's `next` reference 
        return self.next_node

    def set_next(self, new_next):
        # sets this node's `next` reference to `new_next`
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # the first Node in the LinkedList
        self.head = None
        # the last Node in the LinkedList
        self.tail = None

    '''
    Adds `data` to the end of the LinkedList 
    O(1) because this operation doesn't depend on the size of the linked list 
    '''
    def add_to_tail(self, data):
        # wrap the `data` in a Node instance 
        new_node = Node(data)

        # what about the empty case, when both self.head = None and self.tail = None?
        if not self.head and not self.tail:
            # list is empty 
            # update both head and tail to point to the new node 
            self.head = new_node
            self.tail = new_node
        # non-empty linked list case 
        else:
            # call set_next with the new_node on the current tail node 
            self.tail.set_next(new_node)
            # update self.tail to point to the new last Node in the linked list 
            self.tail = new_node

    '''
    Removes the Node that `self.tail` is referring to and returns the 
    Node's data

    What's the runtime of this method?
    '''
    def remove_tail(self):
        # if the linked list is empty 
        if self.tail is None:
            return None
        # save the tail Node's data
        data = self.tail.get_value()
        # both head and tail refer to the same Node 
        # there's only one Node in the linked list 
        if self.head is self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        else:
            # in order to update `self.tail` to point to the
            # the Node _before_ the tail, we need to traverse
            # the whole linked list starting from the head,
            # because we cannot move backwards from any one
            # Node, so we have to start from the beginning
            current = self.head

            # traverse until we get to the Node right 
            # before the tail Node 
            while current.get_next() != self.tail:
                current = current.get_next()

            # `current` is now pointing at the Node right
            # before the tail Node
            self.tail = None
            self.tail = current
            # self.tail.set_next(None)

        
        return data

    '''
    Removes the Node that `self.head` is referring to and returns the 
    Node's data 
    '''
    def remove_head(self):
        if self.head is None:
            return None
        # save the head Node's data
        data = self.head.get_value()
        # both head and tail refer to the same Node
        # there's only one Node in the linked list 
        if self.head is self.tail:
            # set both to be None 
            self.head = None
            self.tail = None
        else:
            # we have more than one Node in the linked list 
            # delete the head Node 
            # update `self.head` to refer to the Node after the Node we just deleted
            self.head = self.head.get_next()

        return data

    '''
    Traverses the linked list and returns a boolean indicating whether the 
    specified `data` is in the linked list.

    What's the runtime for this method?
    '''
    def contains(self, data):
        # an empty linked list can't contain what we're looking for 
        if not self.head:
            return False

        # get a reference to the first Node in the linked list 
        # we update what this Node points to as we traverse the linked list 
        current = self.head 

        # traverse the linked list so long as `current` is referring 
        # to a Node 
        while current is not None:
            # check if the Node that `current` is pointing at is holding
            # the data we're looking for 
            if current.get_value() == data:
                return True
            # update our `current` pointer to point to the next Node in the linked list
            current = current.get_next()
        
        # we checked the whole linked list and didn't find the data
        return False

    '''
    Traverses the linked list, fetching the max value in the linked list

    What is the runtime of this method?
    '''
    def get_max(self):
        if self.head is None:
            return None

        max_so_far = self.head.get_value()

        current = self.head.get_next()

        while current is not None:
            if current.get_value() > max_so_far:
                max_so_far = current.get_value()

            current = current.get_next()

        return max_so_far

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_tail()

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_head()

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the value to the root's value to determine which direction
        # we're gonna go in 
        # if the value < root's value 
        if value < self.value:
            # go left 
            # how do we go left?
            # we have to check if there is another node on the left side
            if self.left: 
                # then self.left is a Node 
                # now what?
                self.left.insert(value)
            else:
                # then we can park the value here
                self.left = BSTNode(value)
        # else the value >= root's value 
        else:
            # go right
            # how do we go right? 
            # we have to check if there is another node on the right side 
            if self.right:
                # then self.right is a Node 
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if target == self.value
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            # return the max int in the right tree.
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        print(self.value)
        fn(self.value)
        if self.left:
            print('left')
            self.left.for_each(fn)
        if self.right:
            print('right')
            self.right.for_each(fn)
        else:
            return None
            
    # Part 2 -----------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        
        if self.right:
            self.right.in_order_print(self.right)

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while len(queue) > 0:
            next_node: BSTNode = queue.dequeue()
            print(next_node.value)
            if next_node.left:
                queue.enqueue(next_node.left)
            if next_node.right:
                queue.enqueue(next_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while len(stack) > 0:
            next_node: BSTNode = stack.pop()
            print(next_node.value)
            if next_node.left:
                stack.push(next_node.left)
            if next_node.right:
                stack.push(next_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass