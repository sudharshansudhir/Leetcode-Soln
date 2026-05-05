# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        l=1
        tail=head
        while tail.next:
            tail=tail.next
            l+=1
        
        k=k%l
        if k==0:
            return head
        tail.next=head
        # k=k%l
        j=l-k-1
        newh=head
        for i in range(j):
            newh=newh.next
        newhead=newh.next
        newh.next=None
        return newhead

