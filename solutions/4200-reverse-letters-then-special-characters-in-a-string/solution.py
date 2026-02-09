class Solution:
    def reverseByType(self, s: str) -> str:
        strs=[]
        sym=[]
        for i in s:
            if i.isalpha():
                strs.append(i)
            else:
                sym.append(i)
        left=0
        right=len(sym)-1
        while left<right:
            sym[left],sym[right]=sym[right],sym[left]
            left+=1
            right-=1
        left=0
        right=len(strs)-1
        while left<right:
            strs[left],strs[right]=strs[right],strs[left]
            left+=1
            right-=1
        print(strs,sym)
        i=0
        j=0
        ans=""
        for k in s:
            if k.isalpha():
                ans+=strs[i]
                i+=1
            else:
                ans+=sym[j]
                j+=1
        return ans
