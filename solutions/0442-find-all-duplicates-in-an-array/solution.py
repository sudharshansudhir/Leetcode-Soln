class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict={}
        for i in nums:
            if i in dict.keys():
                dict[i]=dict[i]+1
            else:
                dict[i]=1
        c=[]
        for k,v in dict.items():
            if dict[k]==2:
                c.append(k)
        return c
