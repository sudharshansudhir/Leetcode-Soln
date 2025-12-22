class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        num=str(num)
        for i in range(len(num)):
            if(int(num)%int(num[i])==0):
                c+=1
        
        return c

        
