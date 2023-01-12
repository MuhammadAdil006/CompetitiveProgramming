# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head2=head
        while head2 and head2.val==val:
            head2=head2.next
        head=head2
        def recurse(head,val):
            if head==None:
                return
            else:
                if head.next and head.next.val==val:
                    head.next=head.next.next
                    recurse(head,val)
                else:
                    recurse(head.next,val)
            return head
        return recurse(head,val)