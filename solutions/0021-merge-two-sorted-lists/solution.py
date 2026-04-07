# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=[]
        l2=[]
        lat1=list1
        lat2=list2
        while lat1:
            l1.append(lat1.val)
            lat1=lat1.next
        while lat2:
            l2.append(lat2.val)
            lat2=lat2.next
        
        l3=l1+l2
        l3.sort()
        newNode=None
        for i in l3:
            if not newNode:
                newNode=ListNode(i)
            else:
                last=newNode
                while last.next:
                    last=last.next
                last.next=ListNode(i)
        return newNode
