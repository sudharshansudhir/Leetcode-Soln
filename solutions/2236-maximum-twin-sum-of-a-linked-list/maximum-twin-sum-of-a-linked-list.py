# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        t=head
        while t:
            arr.append(t.val)
            t=t.next
        rev=arr[::-1]
        s=0
        for i in range(len(arr)):
            s=max(s,arr[i]+rev[i])
        return s