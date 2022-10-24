class Node:
        def __init__(self, val):
                self.key = val
                self.left = self.right =None

def insert(node, key):
		if (node==None):
				return Node(key)

		if key > node.key:
				node.right = insert(node.right, key)
		if key <= node.key:
				node.left = insert(node.left, key)
		return node


def binary_treesort(arr):
		if not arr:
				return False
		
		root = insert(None, arr[0])
		for i in range(1, len(arr)):
				root = insert(root, arr[i])

		# inorder traversal
		stack =[]
		inorder_traversal(root, stack)
		return stack
		
def inorder_traversal(root, stack):
		if root is not None:
				inorder_traversal(root.left, stack)
				stack.append(root.key)
				inorder_traversal(root.right, stack)

arr = [1, 5, 8, 19, 6]
print(binary_treesort(arr))