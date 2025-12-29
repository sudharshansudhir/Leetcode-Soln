class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=[]
        for i in nums1:
            ind=nums2.index(i)
            # print(ind)
            if(ind>=0):
                yes=False
                # print("---",ind+1,len(nums2))
                for j in range(ind+1,len(nums2)):
                    # print(nums2[j])
                    # print("...",nums2[j],i)
                    if(nums2[j]>i and not yes):
                        s.append(nums2[j])
                        yes=True
                if(not yes):
                    s.append(-1)
        return s
                    
