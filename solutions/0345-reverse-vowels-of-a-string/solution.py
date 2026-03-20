class Solution:
    def reverseVowels(self, s: str) -> str:
        vow=[]
        for i in s:
            if i in "aeiouAEIOU":
                vow.append(i)
        vow=vow[::-1]
        an=""
        k=0
        for i in s:
            if i in "aeiouAEIOU":
                an+=vow[k]
                k+=1
            else:
                an+=i
        return an


