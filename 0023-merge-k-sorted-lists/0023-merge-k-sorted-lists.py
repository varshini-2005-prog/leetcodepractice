# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for i in lists:
            while i !=None:
                arr.append(i.val)
                i=i.next

        arr.sort()
        dum=ListNode(0)
        temp=dum
        for val in arr:
            temp.next=ListNode(val)
            temp=temp.next
        return dum.next