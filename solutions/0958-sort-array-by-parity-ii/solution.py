class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        ans=[]
        # j=0
        # k=0
        for i in range(len(nums)):
            if i%2==0:
                p=even.pop()
                ans.append(p)
            else:
                p=odd.pop()
                ans.append(p)
        return ans


            
