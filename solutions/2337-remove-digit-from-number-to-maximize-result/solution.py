class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans=[]
        ind=[]
        t=""
        for i in range(len(number)):
            if(number[i]==digit):
                t=number[:i]+number[i+1:]
                ans.append(int(t))

        print(ans)
        return str(max(ans))
