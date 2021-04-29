
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    @staticmethod
    def display(head):
        current = head      # Start with header

        while current:                      # If a node is present
            print(current.data, end=' ')    # Display current node's data
            current = current.next          # View the next node

    @staticmethod
    def insert(head, data):
        new_node = Node(data)       # Takes data from node

        if not head:                # If it's not the header return it's data
            return new_node

        current = head              # Current node being viewed is now the header

        while current.next:         # If there is another node
            current = current.next  # View the next node

        current.next = new_node     # Fetch the next nodes data

        return head


if __name__ == '__main__':
    my_list = Solution()
    T = int(input())
    head_pointer = None

    for i in range(T):
        data = int(input())
        head = my_list.insert(head_pointer, data)

    my_list.display(head_pointer)
