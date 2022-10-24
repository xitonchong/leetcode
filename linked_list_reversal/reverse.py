class Node:
    def __init__(self, value):
        self.next = None
        self.data = value


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head   #update previous head as next to new node
        self.head = new_node  # head is now at new node


    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp: 
            linkedListStr = (linkedListStr + str(temp.data) + " ")
            temp = temp.next 
        return linkedListStr

    

    def reverse(self):
        current = self.head
        prev = None
        
        while current is not None:
            next = current.next
            current.next = prev 

            prev = current
            current = next
        self.head = prev


linkedList = LinkedList()
linkedList.push(20)
linkedList.push(4)
linkedList.push(15)
linkedList.push(85)
 
print("Given linked list")
print(linkedList)

linkedList.reverse()
print(linkedList)