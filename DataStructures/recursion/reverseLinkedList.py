# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recurse(head):
            if head.next==None:
                return head,head
            Node,start=recurse(head.next)
            Node.next=head
            return head,start
        if head:
            Node,start=recurse(head)
            Node.next=None
    
            return start
        return head