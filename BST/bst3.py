class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_height(root):
    if root is None:
        return 0
    else:
        left_height = find_height(root.left)
        right_height = find_height(root.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of the binary tree is: ", find_height(root))