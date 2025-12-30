class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dict={}
        for i in nums1:
            dict[i[0]]=i[1]
        for i in nums2:
            key=dict.keys()
            val=0
            if(i[0] in key):
                val=dict[i[0]]

            dict[i[0]]=i[1]+val
        ke=dict.keys()
        kee=[]
        for i in ke:
            kee.append(i)
        # print(ke)
        kee.sort()
        ans=[]
        for i in kee:
            ans.append([i,dict[i]])
        return ans
