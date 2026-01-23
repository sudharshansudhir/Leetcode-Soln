class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if(len(nums1)<=len(nums2)):
            m1=nums1[:]
            m2=nums2[:]
        else:
            m1=nums2[:]
            m2=nums1[:]

        ans=[]
        for i in m1:
            if i in m2:
                ans.append(i)
                m2.remove(i)
        return ans
