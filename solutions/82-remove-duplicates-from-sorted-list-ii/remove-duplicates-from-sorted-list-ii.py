# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ar=[]
        temp=head
        while temp:
            ar.append(temp.val)
            temp=temp.next
        arr=[]
        d={}
        for i in ar:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        for k,v in d.items():
            if v==1:
                arr.append(k)
        # arr.sort()
        h1=None
        t=None
        for i in arr:
            if h1==None:
                h1=ListNode(i)
                t=h1
            else:
                t.next=ListNode(i)
                t=t.next
        return h1
