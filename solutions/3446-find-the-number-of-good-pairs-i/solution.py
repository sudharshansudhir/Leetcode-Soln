class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                t=nums1[i]//(nums2[j]*k)
                if nums1[i]/(nums2[j]*k)==t:
                    # print((nums2[j]*2)/nums1[i],t)
                    ans.append([j,i])
        # print(ans)
        return len(ans)

