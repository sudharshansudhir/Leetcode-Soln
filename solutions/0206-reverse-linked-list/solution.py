# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=None
        last=head
        node=None
        while last:
            if not node:
                node=last
                last=last.next
                node.next=None
                temp=node
            else:
                node=last
                last=last.next
                node.next=temp
                temp=node
                
        return node
