class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        cm=list(set(list1).intersection(set(list2)))
        m=float('inf')
        ans=[]
        for i in cm:
            l1=list1.index(i)
            l2=list2.index(i)
            m=min(m,l1+l2)
        for i in cm:
            l1=list1.index(i)
            l2=list2.index(i)
            if l1+l2==m:
                ans.append(i)
        return ans
        
