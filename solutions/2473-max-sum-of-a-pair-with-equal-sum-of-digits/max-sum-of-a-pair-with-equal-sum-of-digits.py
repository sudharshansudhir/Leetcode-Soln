class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            s=sum(list(map(int,list(str(i)))))
            if s in dict.keys():
                # print(dict[s])
                dict[s].append(i)
            else:
                dict[s]=[i]
        # print(dict)
        val=list(dict.values())
        val.sort(key=len)
        m=-1
        for i in val:
            if len(i)>1:
                i.sort(reverse=True)
                m=max(m,sum(i[:2]))
        return m