class Solution:
    def reverseVowels(self, s: str) -> str:
        vow=[]
        for i in s:
            if i in "aeiouAEIOU":
                vow.append(i)
        vow=vow[::-1]
        ans=""
        j=0
        for i in s:
            if not i in "aeiouAEIOU":
                ans+=i
            else:
                ans+=vow[j]
                j+=1
        return ans
