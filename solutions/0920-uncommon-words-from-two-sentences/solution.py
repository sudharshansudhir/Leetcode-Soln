class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split()
        s2=s2.split()
        s1.extend(s2)
        # print(s1)
        ans=[]
        for i in range(len(s1)):
            print(s1[i],s1[i+1:])
            ss=s1[:i]+s1[i+1:]
            if (s1[i] not in ss):
                ans.append(s1[i])
        return ans
        
