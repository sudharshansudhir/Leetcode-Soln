class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ans=[]
        k=0
        i=0
        while i<len(nums1) and k<len(nums2):
            if nums1[i]==nums2[k]:
                return nums1[i]
            elif nums1[i]>nums2[k]:
                k+=1
            else:
                i+=1
        return -1

