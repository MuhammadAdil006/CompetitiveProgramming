from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printee(root):
    while root:
        print(root.val)
        root = root.next
    print(" ")


def reverse(head):
    pre = None
    cur = head
    next = None
    while (cur != None):
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    node = pre
    return node


def reorder(head):
    stack = deque()
    # finding middle node
    slow = head
    fast = head.next
    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    # splitting linked list
    node1 = head
    node2 = slow.next
    slow.next = None
    # reversing the second list
    node2 = reverse(node2)
    # mergin the two list
    while node1 and node2:
        cur1=node1.next
        cur2=node2.next
        node1.next=node2
        node2.next=cur1
        node1=cur1
        node2=cur2
    printee(head)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

reorder(head)
