class Solution:
    def frequencySort(self, s: str) -> str:
        dict={}
        for i in s:
            if i in dict.keys():
                dict[i]=dict[i]+1
            else:
                dict[i]=1
        c=[]
        for k,v in dict.items():
            c.append([k,v])
        c.sort(key=lambda x:x[1])
        c=c[::-1]
        t=""
        for i in c:
            t+=i[0]*i[1]
        return t

