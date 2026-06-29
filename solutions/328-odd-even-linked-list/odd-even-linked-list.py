# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=even=[]
        oh=ot=None
        nh=nt=None
        t=head
        ind=1
        while t:
            if not ind%2==0:
                if not oh:
                    oh=ListNode(t.val)
                    ot=oh
                else:
                    ot.next=ListNode(t.val)
                    ot=ot.next
            else:
                if not nh:
                    nh=ListNode(t.val)
                    nt=nh
                else:
                    nt.next=ListNode(t.val)
                    nt=nt.next
            ind+=1
            t=t.next
        if ot:
            ot.next=nh
        return oh