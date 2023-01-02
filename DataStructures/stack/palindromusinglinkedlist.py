
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    stack = deque()
    root = head
    while (head):
        stack.append(head.val)
        head = head.next
    stack2 = deque()
    i = len(stack)//2
    for j in range(i):
        stack2.append(stack.pop())
    if (len(stack) != len(stack2)):
        stack.pop()
    while (True):
        if (len(stack) == 0 or len(stack2) == 0):
            break
        if (stack.pop() != stack2.pop()):
            return False
    if len(stack) == 0 and len(stack2) == 0:
        return True
    return False


head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(0)
# head.next.next.next = ListNode(1)
print(isPalindrome(head))
