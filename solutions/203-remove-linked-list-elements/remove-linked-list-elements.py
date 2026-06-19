# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp=head
        while head and val==head.val:
            head=head.next
            temp=head

        prev=None
        while temp:
            prev=temp
            temp=temp.next
            while temp and temp.val==val:
                prev.next=temp.next
                temp=temp.next
        return head
            