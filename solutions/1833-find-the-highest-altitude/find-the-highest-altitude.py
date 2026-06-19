class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s=0
        arr=[0]
        for i in range(len(gain)):
            arr.append(arr[-1]+gain[i])
        return max(arr)