import sys
sys.set_int_max_str_digits(10000)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=""
        for i in num:
            s+=str(i)
        s=int(s)+k
        s=str(s)
        ans=[]
        for i in s:
            ans.append(int(i))
        return ans