
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

    def get_height(self, root):
        if not root:        # If there in no tree, the height is -1
            return -1

        if not root.left and not root.right:    # If there is only one node in the tree
            return 0                            # its height is 0

        left_height = self.get_height(root.left)    # Recursive calls on the left and right
        right_height = self.get_height(root.right)  # nodes until the height is zero

        return max(left_height, right_height) + 1   # The height is the longest branch


if __name__ == '__main__':
    T = int(input())
    myTree = Solution()
    my_root = None

    for _ in range(T):
        my_data = int(input())
        my_root = myTree.insert(my_root, my_data)

    height = myTree.get_height(my_root)
    print(height)
