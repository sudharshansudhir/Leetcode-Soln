class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        rt=[]
        lt=[]
        mi=[]
        for i in nums:
            if i <pivot:
                rt.append(i)
            elif(i==pivot):
                mi.append(i)
            else:
                lt.append(i)
        return rt+mi+lt
