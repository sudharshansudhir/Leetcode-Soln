class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans=[]
        for i in words:
            d={}
            k=[]
            l=[]
            flag=True
            for j in range(len(i)):
                if pattern[j] not in k and i[j] not in l:
                    k.append(pattern[j])
                    l.append(i[j])
                    d[pattern[j]]=i[j]
                else:
                    key=d.keys()
                    if pattern[j] in key and d[pattern[j]]==i[j]:
                        continue
                    else:
                        flag=False
                        break
            if(flag):
                ans.append(i)
        return ans


