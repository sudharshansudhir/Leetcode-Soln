import sys
sys.set_int_max_str_digits(10000)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=""
        t=head
        while t:
            arr+=str(t.val)
            t=t.next
        arr=str(int(arr)*2)
        nh=None
        nt=None
        for i in arr:
            if not nh:
                nh=ListNode(int(i))
                nt=nh
            else:
                nt.next=ListNode(int(i))
                nt=nt.next
        return nh
