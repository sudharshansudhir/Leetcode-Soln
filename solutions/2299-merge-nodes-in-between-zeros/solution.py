# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        curr=None
        head1=None
        t=0
        ans=[]
        while temp.next:
            if temp.val==0 and t:
                ans.append(t)
                t=0
            t+=temp.val
            temp=temp.next
        if t:
            ans.append(t)
        for i in ans:
            if not curr:
                curr=ListNode(i)
                temp=curr
            else:
                temp.next=ListNode(i)
                temp=temp.next
        return curr
        
