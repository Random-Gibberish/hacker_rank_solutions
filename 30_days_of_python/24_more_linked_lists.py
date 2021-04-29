
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        """ Inserts the input data into the tree """

        p = Node(data)

        if not head:            # If there is no header
            head = p                # the node data becomes the header
        elif not head.next:
            head.next = p           # The next node is assigned the node data
        else:
            start = head

            while start.next:       # Whilst there is a next node
                start = start.next      # Current node is assigned the next node

            start.next = p          # Next node is assigned the node data

        return head

    def display(self, head):
        """ Prints the data in the current node """

        current = head

        while current:                      # Whilst there is a header
            print(current.data, end=' ')    # print its data
            current = current.next          # and update the node

    def remove_duplicates(self, head):
        """ Removes duplicates in the tree """

        if not head:        # If there is no data the task is finished
            return None

        current = head

        while current.next:                         # Whilst there is a next node
            if current.next.data == current.data:   # if its data is equal to that of the previous node
                current.next = current.next.next    # it is assigned to the node after it
            else:
                current = current.next      # Otherwise update the current node

        return head


if __name__ == '__main__':
    my_list = Solution()
    T = int(input())
    my_head = None

    for _ in range(T):
        my_data = int(input())
        my_head = my_list.insert(my_head, my_data)

    head = my_list.remove_duplicates(my_head)
    my_list.display(head)
