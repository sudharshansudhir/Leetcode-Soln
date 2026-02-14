class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs.sort(key=len)
        w=strs[0]
        for i in range(len(w)):
            flag=True
            t=""
            for j in range(1,len(strs)):
                if w[i]==strs[j][i]:
                    continue
                else:
                    flag=False
                    break
            if(flag):
                ans+=w[i]
            else:
                return ans
        print(ans)
        return ans

