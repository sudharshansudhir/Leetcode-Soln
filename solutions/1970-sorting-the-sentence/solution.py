class Solution:
    def sortSentence(self, s: str) -> str:
        dict={}
        ar=[]
        s=s.split()
        for i in s:
            dict[int(i[-1])]=i[:len(i)-1]
            ar.append(int(i[-1]))
        ar.sort()
        ans=""
        for i in ar:
            ans+=dict[i]
            ans+=" "
        return ans.strip()
