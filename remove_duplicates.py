# Given the head of a sorted singly linked list, eliminate any duplicate elements, 
# ensuring each value in the list is unique. The resulting linked list must remain 
# sorted. Modify the linked list and return the head of the revised, duplicate-free list.

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

def deleteDuplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head


list1 = createLinkedList([1, 1, 2])
list2 = createLinkedList([1, 1, 2, 3, 3])
list3 = createLinkedList([1, 2, 3, 3, 4])
list4 = createLinkedList([2, 2, 2, 3, 3])
list5 = createLinkedList([5])

printLinkedList(deleteDuplicates(list1)) # Expected: "1 -> 2 -> null"
printLinkedList(deleteDuplicates(list2)) # Expected: "1 -> 2 -> 3 -> null"
printLinkedList(deleteDuplicates(list3)) # Expected: "1 -> 2 -> 3 -> 4 -> null"
printLinkedList(deleteDuplicates(list4)) # Expected: "2 -> 3 -> null"
printLinkedList(deleteDuplicates(list5)) # Expected: "5 -> null"