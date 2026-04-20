# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]

        def traverse(head):
            if head:
                temp=head
                while temp:
                    arr.append(temp.val)
                    temp=temp.next
        def createNode(val,head):
            temp=head
            while temp.next:
                temp=temp.next
            temp.next=ListNode(val)
        for i in lists:
            traverse(i)
        
        if arr:
            arr.sort()
            c=ListNode(arr[0])
            for i in range(1,len(arr)):
                createNode(arr[i],c)
            print(c)
            return c
        # else:
        #     return []
