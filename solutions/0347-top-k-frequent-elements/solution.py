class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans={}
        for i in nums:
            if i not in ans.keys():
                ans[i]=1
            else:
                ans[i]=ans[i]+1
        dic=dict(sorted(ans.items(),key=lambda x:x[1],reverse=True))
        a=[]
        key=[]
        c=0
        for i,v in dic.items():
            key.append(i)
            c+=1
            if c==k:
                return key
        # for i in range(k):

