class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def path_from_root(root, key, hist=[]):
    if root is None:
        return None
    else:
        hist.append(root.value)
        #print('appending node ', root.value, hist)
        if root.value == key:
            #print('jackpot')
            return True
        elif root.value < key:
            if path_from_root(root.left, key, hist):
                return hist
        else: #root.value > key:
            if path_from_root(root.right, key, hist): 
                return hist
    # if the below return is ommited, this function will return None as hist passed at the midstage still has some stages to traverse
    #return hist

    # it is useful to return bool to the function
    # as it will give information on whether the traverse hit the jackpot 


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
r = insert(r, 50)
r = insert(r, 88)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)



# Print inoder traversal of the BST
inorder(r)

key = 70
print(key, 'path from root ', path_from_root(r, key, [] ))
key = 80
print(key, 'path from root ', path_from_root(r, key, []))
key = 66
print(key, 'path from root ', path_from_root(r, key, []))
key = 20
print(key, 'path from root ', path_from_root(r, key, []))