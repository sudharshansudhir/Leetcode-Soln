class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1+=nums2
        for i in range(len(nums1)-1):
            for j in range(i+1,len(nums1)):
                if(nums1[i]>nums1[j]):
                    t=nums1[i]
                    nums1[i]=nums1[j]
                    nums1[j]=t
        while 0 in nums1:
            if((nums1[0]==0 and not len(nums1)==m+n) or len(nums1)>m+n):
                nums1.remove(0)
            else:
                break
