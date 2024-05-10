# Given two sorted singly linked lists, your task is to combine them into a single sorted linked list. 
# The new list should be composed of the nodes from the two original lists and should also be sorted in 
# ascending order (where node values are equal to or increase as you move through the linked list).

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(arr):
    head = ListNode(0)
    current = head
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    
    return head.next

def printLinkedList(head):
    curr = head
    return_str = ''
    while curr != None:
        return_str += str(curr.val) + ' -> '
        curr = curr.next
    return_str += 'None'
    print(return_str)

def mergeSortedLists(list1, list2):
    dummy = ListNode()
    curr = dummy

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        
        curr = curr.next
    
    if list1:
        curr.next = list1
    else:
        curr.next = list2

    return dummy.next
            

list1 = createLinkedList([1, 3, 5])
list2 = createLinkedList([2, 4, 6])
printLinkedList(mergeSortedLists(list1, list2)) # Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null

list3 = createLinkedList([1, 2, 3])
list4 = createLinkedList([])
printLinkedList(mergeSortedLists(list3, list4)) # Expected: 1 -> 2 -> 3 -> null

list5 = createLinkedList([])
list6 = createLinkedList([1])
printLinkedList(mergeSortedLists(list5, list6)) # Expected: 1 -> null

list7 = createLinkedList([1, 5, 9])
list8 = createLinkedList([2, 4, 6, 8, 10])
printLinkedList(mergeSortedLists(list7, list8)) # Expected: 1 -> 2 -> 4 -> 5 -> 6 -> 8 -> 9 -> 10 -> null

list9 = createLinkedList([1, 2, 5])
list10 = createLinkedList([3, 6, 7])
printLinkedList(mergeSortedLists(list9, list10)) # Expected: 1 -> 2 -> 3 -> 5 -> 6 -> 7 -> null