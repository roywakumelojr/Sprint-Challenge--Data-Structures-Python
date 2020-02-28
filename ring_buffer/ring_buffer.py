from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Checks the status of the contents to ensure the capacity is greater than the length
        if self.capacity > self.storage.length:
            # If the capacity is greater then the length, add the new item to the head
            self.storage.add_to_head(item)
            # Points the item to itself in-order to complete the 360 degree buffer ring
            self.current = self.storage.tail
        else:
            # Else, if there is an existing value. Assign current value to item
            self.current.value = item

            # If the current stored value is the head:
            if self.current is self.storage.head:
                # Point the tail to the head in order to over write the default of none
                self.current = self.storage.tail
            else:
                # Else, move a step forward and set the current item as the new previous
                self.current = self.current.prev

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # Check for status of the item on the tail
        last_node_item = self.storage.tail

        # If the tail item is not None
        while last_node_item is not None:

            # Add the value to the list and set it as the new previous
            list_buffer_contents.append(last_node_item.value)
            last_node_item = last_node_item.prev

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
