class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        dict={}
        mini=float('inf')

        for i,num in enumerate(nums):
            rev=int(str(num)[::-1])
            # if num in [1,10,100,1000,10000]:
            #     num=1

            if num in dict:
                mini=min(mini,i-dict[num])
            dict[rev]=i
        # print(dict)
        return mini if not mini==float('inf') else -1


