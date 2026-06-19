# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr=[]
        t=head
        while t:
            arr.append(t.val)
            t=t.next
        lt=arr[:left-1]
        mid=arr[left-1:right]
        rit=arr[right:]
        arr=lt[:]+mid[::-1]+rit[:]
        newHead=None
        tail=None
        for i in arr:
            if not newHead:
                newHead=ListNode(i)
                tail=newHead
            else:
                tail.next=ListNode(i)
                tail=tail.next
        return newHead