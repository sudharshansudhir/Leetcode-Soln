# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=[]
        temp=head
        while temp.next:
            v1=temp.val
            v2=temp.next.val
            a=math.gcd(v1,v2)
            newNode=ListNode(a)
            newNode.next=temp.next
            temp.next=newNode
            temp=temp.next.next
        return head

