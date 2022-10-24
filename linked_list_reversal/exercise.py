

# define Node class

# define single linked list class
# implement push and reverse method 

class Node:
    def __init__(self, value):
        self.next = None  #pointers
        self.data = value 



class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        #head is assigned to last come in item
        new_node = Node(value)
        new_node.next = self.head # point new node pointer to previous elements
        # update self.head
        self.head = new_node 

    def __str__(self):
        node = self.head
        stack = []
        while node:
            stack.append(str(node.data))
            node = node.next 

        return ' -> '.join(stack)
        

    def reverse(self):
        prev = None
        node = self.head 

        while node:
            next = node.next # get the next node
            node.next = prev # point node.next to previous node

            prev = node 
            node = next 
        
        # next will be None 
        self.head = prev

    def reverseRecursive(self):
        if self.head is None:
            return None

        self.recursive(None, self.head)


    def recursive(self, prev, current):
        if current.next is None:
            self.head = current
            #update next to prev node
            self.head.next = prev
            return 

        next = current.next
        current.next = prev 
        
        
        self.recursive(current, next)



mylist = range(7)
print(list(mylist))
single_list = LinkedList()

for value in mylist:
    single_list.push(value)

print(single_list)

single_list.reverse()

print(single_list)

single_list.reverseRecursive()
print(single_list)