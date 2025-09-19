class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        no=[]
        yes=[]
        for i in range(1,n+1):
            if(i%m==0):
                yes.append(i)
            else:
                no.append(i)
        t=sum(no)-sum(yes)
        # print(yes)
        # print(no)
        
        return t
