# In this problem, you are given a singly linked list and you need to remove every alternate node, starting with the second node. 
# As you progress through the list, every second node should be deleted until you reach the end of the list.

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

list1 = createLinkedList([1, 2, 3, 4, 5])
list2 = createLinkedList([1, 2])
list3 = createLinkedList([1])
list4 = createLinkedList([1, 2, 3, 4])
list5 = createLinkedList([])

def removeEverySecondNode(head):
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        if curr.val % 2 == 0:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
        

    return dummy.next

printLinkedList(removeEverySecondNode(list1)) # Expected: 1 -> 3 -> 5 -> None
printLinkedList(removeEverySecondNode(list2)) # Expected: 1 -> None
printLinkedList(removeEverySecondNode(list3)) # Expected: 1 -> None
printLinkedList(removeEverySecondNode(list4)) # Expected: 1 -> 3 -> None
printLinkedList(removeEverySecondNode(list5)) # Expected: None