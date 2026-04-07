# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        last=head
        while last:
            n+=1
            last=last.next
        n=n//2
        last=head
        newNode=None
        d=0
        while d<n:
            last=last.next
            d+=1
        return last
                

            



