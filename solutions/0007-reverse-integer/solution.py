class Solution:
    def reverse(self, x: int) -> int:
        ans=""
        t=""
        x=str(x)
        for i in x:
            if(i.isdigit()):
                ans+=i
            else:
                t+=i
        ans=ans[::-1]

        a=int(t+ans)
        if(-2**31>a or a>(2**31)-1):
            return 0
        return a
