class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED

    current_value = self.head
    next_value = None
    previous_value = None

    # If the list is empty, return None
    if current_value is None:
      return None

    # Else, if the current value is aviable
    else:
      while current_value is not None:
        # Set a link that connects it to the next node and another that points to the previous node
        # Swap the values in-order to reverse them 
        next_value = current_value.next_node
        current_value.next_node = previous_value
        previous_value = current_value
        current_value = next_value
        self.head = previous_value


    