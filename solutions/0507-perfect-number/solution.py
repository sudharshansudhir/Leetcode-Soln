class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # num=num//2
        n=str(num)
        if(int(n[-1])%2==1):
            return False
        mid=num//2
        s=[]
        for i in range(1,mid+1):
            if(num%i==0):
                s.append(i)
        if(sum(s)==num):
            return True
        return False
