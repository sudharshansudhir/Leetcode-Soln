# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=set()
        temp=head
        while temp:
            arr.add(temp.val)
            temp=temp.next
        h2=None
        t=None
        arr=list(arr)
        arr.sort()
        for i in arr:
            if h2==None:
                h2=ListNode(i)
                t=h2
            else:
                t.next=ListNode(i)
                t=t.next
        return h2