class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            if i in nums2 and not i in ans:
                ans.append(i)
        for i in nums2:
            if i in nums1 and not i in ans:
                ans.append(i)
        return ans

