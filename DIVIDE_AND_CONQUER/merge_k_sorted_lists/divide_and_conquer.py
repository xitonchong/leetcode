
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]

from typing import List, Optional 

class ListNode:
    def __init__(self, value, next1=None):
        self.value = value
        self.next = next1

def array_to_linkedlist(array)-> Optional[ListNode]:
    p = d = ListNode(None)
    for a in array:
        d.next = ListNode(a)
        d = d.next 
    return p.next 

def print_ll(ll: ListNode):
    while ll:
        print(ll.value, end=' ')
        ll = ll.next 
    print('\n')

def mergeKList(lists: List[Optional[ListNode]])-> Optional[ListNode]: 
    if len(lists) == 0:  # won't go here unless lists is empty
        return None 
    if len(lists) == 1:
        return lists[0]
    mid = len(lists) // 2
    l, r = mergeKList(lists[:mid]), mergeKList(lists[mid:])
    return merge(l, r)


def merge(l, r):
    #merge list no 1 and 2
    p = dummy = ListNode(None) # initiating two variable is important, one is use to iterate to end of link, while the other is referenced to the head 
    while l and r:
        # left and right lists, may be of unequal length
        if l.value < r.value:
            dummy.next = l
            l = l.next 
        else:
            dummy.next = r
            r = r.next 
        dummy = dummy.next 
    # if unequal length
    dummy.next = l or r 
    return p.next 


array = [[1,2,3], [1,5,7], [2,5,6]]
ll = array_to_linkedlist(array[0])
print_ll(ll)

ll_array = [array_to_linkedlist(array[0]),
            array_to_linkedlist(array[1]),
            array_to_linkedlist(array[2]),
        ]

result = mergeKList(ll_array)
print_ll(result )