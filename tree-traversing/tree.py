import numpy as np

''' construct a class of binary tree '''

class node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val



''' refer to .gif for the tree structure
    there are 3 types of tree traversing algorithm, 
    1.  in-order :  left->root->right branch
    2.  pre-order:  root->left->right branch
    3.  post-order: left->right->root

    remember the state of the stack for each recursive call
'''

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

def in_order(root):
    # only process when node is not None
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)

def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)

if __name__ == '__main__':
    print("in order tree traversing")
    print("good for printing the value in ascending order if tree follow binary tree property")
    in_order(root)
    print("pre order tree traversing")
    print(" prefix notation?")
    pre_order(root)
    print("post order tree traversing")
    print("delete leaf, operation etc.")
    post_order(root)

