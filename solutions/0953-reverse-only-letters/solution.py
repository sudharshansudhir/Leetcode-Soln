class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans=""
        for i in s:
            if i.isalpha():
                ans+=i
        ans=ans[::-1]
        res=""
        k=0
        for i in s:
            if(i.isalpha()):
                res+=ans[k]
                k+=1
            else:
                res+=i
        return res
