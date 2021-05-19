class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self) -> str:
        """
        Print the list information
        """
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

    def to_list(self):
        """
        Return a list with linked list nodes
        """
        arr = []
        if self.head:
            current_node = self.head
            while current_node:
                arr.append(current_node.data)
                current_node = current_node.next
        return arr

    def get_user_by_id(self, user_id):
        """
        Find a user by id 
        """
        current_node = self.head
        while current_node:
            if current_node.data['id'] is user_id:
                return current_node.data
            current_node = current_node.next
        return None 

