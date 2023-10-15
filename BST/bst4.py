class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def countTerminalNodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return countTerminalNodes(root.left) + countTerminalNodes(root.right)

