# from stack import Stack
# from linked_queue import Queue

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
class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                new_node = BSTNode(value)
                self.left = new_node
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                new_node = BSTNode(value)
                self.right = new_node
            else:
                self.right.insert(value)
                
    def contains(self, target, array):
        if target == self.value:
            array.append(target)
            return True
        if target < self.value and self.left:
            return self.left.contains(target, array)
        if target > self.value and self.right:
            return self.right.contains(target, array)
        return False

    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value

    def for_each(self, fn):
        current = self
        if self is None:
            return
        fn(self.value)
        if current.left:
            current.left.for_each(fn)
        if current.right:
            current.right.for_each(fn)

    def in_order_append(self, node, array):
        if node.left:
            self.in_order_append(node.left, array)
        if node:
            array.append(node.value)
        if node.right:
            self.in_order_append(node.right, array)

    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    # Solved using a list

    # def bft_print(self, node):
    #     if node is None:
    #         return
    #     queue = list()
    #     queue.append(node)
    #     while len(queue) > 0:
    #         print(queue[0].value)
    #         current = queue.pop(0)
    #         if current.left:
    #             queue.append(current.left)
    #         if current.right:
    #             queue.append(current.right)

    # solved using a while loop

    def bft_print(self, node):
        if node is None:
            return
        queue = Queue()
        queue.enqueue(node)
        while queue.__len__() > 0:
            node = queue.dequeue()
            print(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    # Solved using a list

    # def dft_print(self, node):
    #     if node is None:
    #         return
    #     stack = list()
    #     stack.append(node)
    #     while len(stack) > 0:
    #         print(stack[-1].value)
    #         current = stack.pop()
    #         if current.left:
    #             stack.append(current.left)
    #         if current.right:
    #             stack.append(current.right)
    
    # Solved using while loop 

    # def dft_print(self, node):
    #     if node is None:
    #         return
    #     stack = Stack()
    #     stack.push(node)
    #     while stack.__len__() > 0:
    #         node = stack.pop()
    #         print(node.value)
    #         if node.left:
    #             stack.push(node.left)
    #         if node.right:
    #             stack.push(node.right)

    # Solved using recursion

    def dft_print(self, node):
        if node:
            print(node.value)
            self.dft_print(node.left)
            self.dft_print(node.right)
        
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)
            
            
            
