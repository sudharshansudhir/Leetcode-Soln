class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans=abs(dividend)//abs(divisor)

        print(ans)
        if(dividend<-1 and divisor==-1):
            return ans-1
        if(divisor<0 and dividend>0):
            return -ans
        elif(divisor>0 and dividend<0):
            return -ans
        # if()
        return ans

