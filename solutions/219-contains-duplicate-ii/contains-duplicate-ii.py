class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # k+=1
        dict={}
        for ind,val in enumerate(nums):
            if val in dict.keys():
                if abs(dict[val][-1]-ind)<=k:
                    return True
                else:
                    dict[val].append(ind)
            else:
                dict[val]=[ind]
        return False