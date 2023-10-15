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

def inorder(root):
    res = []
    if root:
        res = inorder(root.left)
        res.append(root.val)
        res = res + inorder(root.right)
    return res

def inorder__descending(root):
    return inorder(root)[::-1]

