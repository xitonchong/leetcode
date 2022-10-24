import numpy as np

# Node class
class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

# Linked list class
class Linked_list:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, new_data):
        ''' head, prev_node and new node'''
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, data):
        ''' traverse until end of list then append'''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 

        # else traverse till th last node
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
    
    ''' delete a node based on value, whatever the position'''
    def deleteNode(self, data):
        temp = self.head

        # if head node holds key
        if (temp is not None):
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
        # if in middle
        while (temp):
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        
        if temp is None:
            return 

        prev.next = temp.next
        temp = None
   
    def getLengthRec(self, node):
        if node is not None:
            return 1 + self.getLengthRec(node.next)
        else:
            return 0

    def getLength(self):
        node = self.head
        return self.getLengthRec(node)

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


''' a node can be added in three ways
    1.  at front of the linked list
    2.  after a given node
    3.  at the end of linked list'''

def calculate_length_of_node(llist):
    node = llist.head
    counter = 0
    while (node is not None):
        counter +=1 
        node = node.next
    return counter

    

if __name__ == '__main__':
    llist = Linked_list()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)
    llist.insert(llist.head.next, 8)
    print("created linked list is: ", llist.printList())
    
    llist.deleteNode(8)
    print("linked list delete of 1: ", llist.printList())
    
    # calculate the length of node #
    print("lenght of linked list is ", calculate_length_of_node(llist))
    
    # calculate the length of node drecursively
    print("recursive solution length of linked list is ", llist.getLength())

