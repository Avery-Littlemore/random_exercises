# Given a singly linked list and a specific value (referred to as the 'key'), your task is to determine how many times this key appears within the linked list. 
# For instance, given a linked list like 1->2->1->2->1->3->1 and a key of 1, the expected result would be 4, as the key 1 appears four times in the list.


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

def countKeyOccurrences(head, key):
    total = 0
    curr = head
    while curr != None:
        if curr.val == key:
            total += 1
        
        curr = curr.next

    # print(total)
    return total

list1 = createLinkedList([1, 2, 1, 2, 1, 3, 1])
list2 = createLinkedList([4, 4, 4, 4])
list3 = createLinkedList([1, 2, 3, 4, 5]);
list4 = createLinkedList([5, 5, 1, 2, 3, 5, 5]);
list5 = createLinkedList([]);
list6 = createLinkedList([1, 2, 3, 1, 1])

# print(list3.val)
# print(list3.next.val)

print(countKeyOccurrences(list1, 1) == 4)
print(countKeyOccurrences(list2, 4) == 4)
print(countKeyOccurrences(list3, 1) == 1)
print(countKeyOccurrences(list4, 5) == 4)
print(countKeyOccurrences(list5, 1) == 0)
print(countKeyOccurrences(list6, 1) == 3)