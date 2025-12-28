class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        n=[]
        a=[]
        t=0
        for i in nums:
            if nums.count(i)>=t and i not in a:
                n.append(nums.count(i))
                a.append(i)
                t=nums.count(i)
        print(a,n)
        ans=0
        if(n):
            m=max(n)
            for i in n:
                if i==m:
                    ans+=i
        return ans
        
        # return sum(n)
     
