class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        ans=[]
        if nums[1]<nums[0]:
            return False
        
        p=q=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1] and not p:
                p=i
            elif nums[i]<nums[i+1] and not q and p:
                q=i
        one=nums[:p+1]
        two=nums[p+1:q+1]
        three=nums[q+1:]
        print(one,two,three)
        o=t=th=True
        for i in range(len(one)-1):
            if one[i]>one[i+1] or one[i]==one[i+1]:
                o=False
        for i in range(len(two)-1):
            if two[i]<two[i+1] or two[i]==two[i+1]:
                print(nums[i])
                t=False
        for i in range(len(three)-1):
            if three[i]>three[i+1] or three[i]==three[i+1]:
                th=False
        print(o,t,th)
        return o and t and th and len(one)>0 and len(two)>0 and len(three)>0

            

