

from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


def construct_tree(arr, root, i, n):
    # base case for recursion
    if (i < n) and (arr[i] is not None) :
        temp = TreeNode(arr[i])
        root = temp 
        root.left = construct_tree(arr, root.left, 2*i+1, n)
        root.right = construct_tree(arr, root.right, 2*i+2, n)
    return root 


def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.val, end=" ")
        inOrder(root.right)


def zigzag_traversal(root):

    queue = deque([root])
    result =[]
    direction = 1

    while queue: 
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right) 
        result.append(level[::direction])
        direction *= -1 

    print(result)
    return result 




root = [3,9,20,None,None,15,7]
#root = [1,2,2,3,3,3,3,4,4]
tree = None
tree = construct_tree(root, tree, 0, len(root))
inOrder(tree) 

zigzag_traversal(tree)




answer = [[3],[20,9],[15,7]]

