# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        temp=head
        while temp:
            c+=1
            temp=temp.next
        
        c=c-n
        if c==0:
            head=head.next
            return head
        k=0
        
        temp=head
        prev=head
        while temp:
            if k==c:
                prev.next=temp.next
                temp=temp.next
                k+=1
            else:
                prev=temp
                temp=temp.next
                k+=1
        return (head)
