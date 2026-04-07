# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nodes=[]

        s1=""
        s2=""
        ll1=l1
        ll2=l2
        while ll1:
            s1+=str(ll1.val)
            # nodes.append(ll1.val+ll2.val)
            ll1=ll1.next
        while ll2:
            s2+=str(ll2.val)
            # nodes.append(ll1.val+ll2.val)
            ll2=ll2.next
        print(s1,s2)
        s1=s1[::-1]
        s2=s2[::-1]
        s3=str(int(s1)+int(s2))
        s3=s3[::-1]
        print(s3)
        newNode=None
        for i in s3:
            i=int(i)
            if newNode is None:
                newNode=ListNode(i)
            else:
                last=newNode
                while last.next:
                    last=last.next
                last.next=ListNode(i)
        return newNode
