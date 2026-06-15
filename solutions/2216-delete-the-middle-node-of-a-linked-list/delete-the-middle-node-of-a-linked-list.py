# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        mid=len(arr)//2
        arr.pop(mid)
        t=None
        tail=None
        for i in arr:
            if not t:
                t=ListNode(i)
                tail=t
            else:
                tail.next=ListNode(i)
                tail=tail.next
        return t

