class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            if i in dict.keys():
                dict[i]+=1
            else:
                dict[i]=1
        for k,v in dict.items():
            if v==1:
                return k
                