class Solution:
    def totalMoney(self, n: int) -> int:
        s=n
        c=1
        while n>7:
            c+=1
            n-=7
        ans=[]
        j=1
        print(n,c)
        for i in range(c):
            k=1
            while j<=s:
                ans.append(i+k)
                j+=1
                k+=1
                if(k>7):
                    break
        print(ans)
        return sum(ans)



        
