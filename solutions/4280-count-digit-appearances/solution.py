class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        c=0
        for i in nums:
            i=str(i)
            if str(digit) in i:
                c+=i.count(str(digit))
        return c
