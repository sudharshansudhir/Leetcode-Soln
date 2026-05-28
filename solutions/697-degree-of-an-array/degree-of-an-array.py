class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            if i in dict.keys():
                dict[i]=dict[i]+1
            else:
                dict[i]=1
        m=0
        key=[]
        for k,v in dict.items():
            
            if v >m:
                m=v
                key=[k]
            elif v==m:
                key.append(k)
        s=[]
        for e in key:
            ind=nums.index(e)
            last=0
            for i in range(ind,len(nums)):
                if nums[i]==e:
                    last=i
            s.append(last-ind+1)
        return min(s)