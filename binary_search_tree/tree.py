class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key



def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value == key:
            return root
        elif root.value < key:
            root.left = insert(root.left, key)
        else: #root.value > key
            root.right = insert(root.right, key)
    return root 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
 
# Print inoder traversal of the BST
inorder(r)