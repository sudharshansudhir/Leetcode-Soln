class Solution:
    def sortVowels(self, s: str) -> str:
        vow=[]
        for i in s:
            if i in "aeiouAEIOU":
                vow.append(i)
        vow.sort()
        print(vow)
        i=0
        ans=""
        for k in s:
            if(k in "aeiouAEIOU"):
                ans+=vow[i]
                i+=1
            else:
                ans+=k
        return ans
                
