
class Node:
    def __init__(self, data):
        self.right = self.left = None   # Initiate both branches as None
        self.data = data


class Solution:
    def insert(self, root, data):
        if not root:        # If there is no node,
            return Node(data)   # the branches are None

        else:
            if data <= root.data:                   # If the current data <= root.data
                cur = self.insert(root.left, data)
                root.left = cur                     # the left root is assigned to the current data
            else:
                cur = self.insert(root.right, data)
                root.right = cur                    # Otherwise the right root is assigned to the current data

        return root

    def level_order(self, root):
        nodes_to_search = []
        nodes_traversed = ''
        nodes_to_search.append(root)

        while len(nodes_to_search) > 0:     # Whilst there are still unchecked nodes
            node = nodes_to_search.pop(0)   # Check the first node

            if node.left:                           # If there is a left node
                nodes_to_search.append(node.left)   # add it to the nodes_to_search list
            if node.right:                          # Same for right node
                nodes_to_search.append(node.right)

            nodes_traversed += str(node.data) + ' '  # Add data to nodes_traversed

        return nodes_traversed


if __name__ == '__main__':
    T = int(input())
    myTree = Solution()
    my_root = None

    for _ in range(T):
        my_data = int(input())
        my_root = myTree.insert(my_root, my_data)

    lev_ord = myTree.level_order(my_root)
    print(lev_ord)
