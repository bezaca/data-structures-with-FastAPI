
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self) -> str:
        ll_string = ""
        current_node = self.head
        while current_node:
            ll_string += f"{str(current_node.data)}->\t"
            current_node = current_node.next
        ll_string += 'None'
        print(ll_string)

    def append(self, data):
        """
        Add the node in the last position
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def prepend(self, data):
        """
        Add the node as the head 
        """
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
