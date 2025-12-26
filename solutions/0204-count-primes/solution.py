class Solution:
    def countPrimes(self, n: int) -> int:
        if(n<=2):
            return 0
        l=[True]*(n)
        p=2
        while p*p<=n:
            if(l[p]):
                for i in range(p*p,n,p):
                    l[i]=False
            p+=1
        ans=[]
        for i in range(2,n):
            if (l[i]):
                ans.append(i)
        # print(ans)
        return len(ans)

