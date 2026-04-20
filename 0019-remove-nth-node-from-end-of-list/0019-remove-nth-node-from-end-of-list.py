# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        temp=head
        while temp!=None:
            c+=1
            temp=temp.next
        if n==c:
            return head.next
        temp=head
        
        for _ in range(c-n-1):
            temp=temp.next
        temp.next=temp.next.next
        return head