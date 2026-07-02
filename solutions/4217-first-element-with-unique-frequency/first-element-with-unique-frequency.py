class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            dict[i]=dict.get(i,0)+1
        print(dict)
        c={}
        for k,v in dict.items():
            # print(c,v,k)
            if v in c.keys():
                c[v].append(k)
            else:
                c[v]=[k]
        # print(c)
        for k,v in c.items():
            if len(v)==1:
                return v[0]
        return -1