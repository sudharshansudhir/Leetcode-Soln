class Solution:
    def convertToBase7(self, num: int) -> str:
        f=False
        if num<0:
            f=True
        if num==0:
            return str(num)
        
        ans=[]
        res=""
        num=abs(num)
        while num>=1:
            res=str(num%7)+res
            num=num//7
        if f:
            return "-"+res
        return res