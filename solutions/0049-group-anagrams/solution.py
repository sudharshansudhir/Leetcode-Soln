class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        dict={}
        for i in range(len(s)):
            a=sorted(list(s[i]))
            t=""
            for e in a:
                t+=e
            if t not in dict.keys():
                dict[t]=[s[i]]
            else:
                dict[t].append(s[i])
        ans=[]
        for k,v in dict.items():
            ans.append(v[:])
        ans.sort(key=lambda x:len(x))
        return ans
