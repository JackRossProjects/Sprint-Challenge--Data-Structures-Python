class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # First check if the list is empty
        if node is None:
            return
        # Check to see is node is the tail (Check if next pointer is null = tail)
        if node.next_node is None:
            # Set the head to the tail node
            self.head = node
            # Set next node to the value passed previously
            node.next_node = prev
            return node
        else:
            # Set the next node in line
            next = node.next_node
            # Update the nodes next_node to the previously passed node
            node.next_node = prev
            # Repeat through the list
            self.reverse_list(next, node)

'''
SOLVE WITHOUT RECURSION

    def reverse_list(self, node, prev):
        current = self.head
        while(current is not None):
            next = current.next_node
            current.next = prev
            prev = current
            current = next
        self.head = prev
'''
