class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        alice=[]
        bob=[]
        for i in range(len(nums)):
            if(nums[i]<10):
                alice.append(nums[i])
            else:
                bob.append(nums[i])
        if(sum(alice)>sum(bob) or sum(bob)>sum(alice)):
            return True
        return False
