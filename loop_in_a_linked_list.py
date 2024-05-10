# Given the starting node (head) of a singly linked list, your task is to find whether the linked 
# list contains a loop. A loop in a linked list exists when a node can be revisited by continuously following the next pointers.

# You should return true if the linked list forms a loop (sometimes referred to as a circular list or a cyclic list) and false if it does not.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(arr, cycle):
    head = ListNode(0)
    current = head
    cycle_node = None

    for index, val in enumerate(arr):
        current.next = ListNode(val)
        current = current.next
        if index == cycle:
            cycle_node = current

    if cycle_node != None:
        current.next = cycle_node
    
    return head.next

def hasCycle(head):
    anchor = head
    runner = head.next

    while runner != None and runner.next != None:
        if anchor.val == runner.val:
            return True
        anchor = anchor.next
        runner = runner.next.next

    return False



list1 = createLinkedList([3, 2, 0, -4], 1)
list2 = createLinkedList([1, 2], 0)
list3 = createLinkedList([1], -1)
list4 = createLinkedList([10, 20, 30, 40, 50, 60], 3)
list5 = createLinkedList([5, 15, 25, 35, 45], -1)

print(hasCycle(list1)) # true
print(hasCycle(list2)) # true
print(hasCycle(list3)) # false
print(hasCycle(list4)) # true
print(hasCycle(list5)) # false
