import sys
sys.path.append('./queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # LECTURE IMPLEMENTATION  
    # def insert(self, value):
    #     # if value < node.value look left
    #     if value < self.value:
    #         # If samething is there already
    #         if self.left:
    #             # recursive left
    #             self.left.insert(value)
    #         # if not
    #         else:
    #             self.left = BinarySearchTree
    #     # If the value is  >= node.value look right
    #     if value >= self.value :
    #         if self.right:
    #             self.right.insert(value)
    #         else:
    #             self.right = BinarySearchTree(value)

    # Insert the given value into the tree
    def insert(self, value):
        # #### Insert Value ####
        # If there is no node at root
        if not BinarySearchTree(value):
            return None

        # Compare value to the root
        # If value is smaller :
        # look left if node, repeat steps
        elif value < self.value: 
            if not self.left: 
                self.left = BinarySearchTree(value)

            #  if no node: Make new one with this value
            else: 
                self.left.insert(value)

        # If value is greater or equal
        # Look right, if node repeat steps
        elif value >= self.value: 
            if not self.right: 
                self.right = BinarySearchTree(value)

            #  if no node: Make new one with this value
            else: 
                self.right.insert(value) 

    # Return True if the tree contains the value
    # False if it does not

    # LECTURE IMPLEMENTATION 
    # def contains(self, target): 
    #     if self.value == target:
    #         return True
    #     if target < self.value:
    #         if self.left:
    #             return self.left.contains(target)
    #         else:
    #             return False
    #     if target >= self.value:
    #         if self.right:
    #             return self.right.contains(target)
    #         else:    
    #             return False

    def contains(self, target):
        #### Find Value ####
        # If no node at root, return false
        if not BinarySearchTree(target):
            return False

        # Compare value to root
        elif self.value == target:
            return True

        # If smaller:
        #     go left: look at node there
        elif target < self.value: 
            if not self.left: 
                return False
            else: 
                return self.left.contains(target)

        # Is greater or ==:
        #     go right
        elif target >= self.value: 
            if not self.right: 
                return False
            else: 
                return self.right.contains(target)

    # Return the maximum value found in the tree

    # LECTURE IMPLEMENTATION 
    # def get_max(self):
    #     if not self.right: 
    #         return self.value
    #     else: 
    #         return self.right.get_max()
    
    def get_max(self):
        #### Get Max ####
        # If no right child, return this value
        if not self.right: 
            return self.value

        # Otherwise, go right
        else: 
            return self.right.get_max()
    

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    # LECTURE IMPLEMENTATION 
    # def for_each(self, cb):
    # #Call callback on self.value
    #     cd(self.value)
    #     # if there is a node on the left, call it
    #     if self.left:
    #         # call for it
    #         self.left.for_each(cb)
    #     # if there is a node on the right, call it
    #     if self.right:
    #         # call for it
    #          self.right.for_each(cb)


    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node:
            return
    
        self.in_order_print(node.left)
        print(node.value)

        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue_content = Queue()
        queue_content.enqueue(self)

        while queue_content.len() != 0:
            node = queue_content.dequeue()
            print(node.value)

            if node.left:
                queue_content.enqueue(node.left)

            elif node.right:
                queue_content.enqueue(node.right)
    
    """
    #### LECTURE NOTES // PSEUDO CODE ####
    ** Breadth First Traversal Steps **
        initialize a queue
        push root to queue
        while stack not empty
        pop top item out of queue into temp
        DO THE THING!!!!!!
        if temp has right right put into queue
        if temp has left left put into queue
    """

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stacks_content = Stack()
        stacks_content.push(node)

        while stacks_content.len() != 0:
            stacks_content.pop()
            print(node.value)

            if node.left:
                stacks_content.push(node.left)

            elif node.right:
                stacks_content.push(node.right)

    """
    #### LECTURE NOTES // PSEUDO CODE ####
    ** Deep First Traversal steps: initialize a stack **
        push root to stack
        while stack not empty
        pop top item out of stack into temp
        DO THE THING!!!!!!
        if temp has right right put into stack
        if temp has left left put into stack
    """

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
