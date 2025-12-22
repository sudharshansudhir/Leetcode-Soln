class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        l=len(str(n))
        if(l==1):return n
        w=100000
        n=str(n)
        ans=[]
        for i in n:
            if(n.count(i)<l):
                w=int(i)
                l=n.count(i)
                ans=[]
            elif(n.count(i)==l):
                ans.append(w)
                # if(not w==0):
                #     ans.append(w)
                ans.append(int(i))
        print(ans)
        if(ans):
            w=min(ans)
        return w
