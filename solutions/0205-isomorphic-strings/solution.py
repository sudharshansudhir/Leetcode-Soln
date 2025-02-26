class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        arr1=[]
        arr2=[]
        for i in range(len(s)):
            if s[i] not in arr1:
                arr1.append(s[i])
            if t[i] not in arr2:
                arr2.append(t[i])
        for i in range(len(s)):
            if arr1.index(s[i])!=arr2.index(t[i]):
                return False
        # for i in range(len(s)-1):
        #     s1=1
        #     t1=1
        #     if s.count(s[i])!=t.count(t[i]):
        #         return False
        #     if s[i]==s[i+1]:
        #         s1+=1
        #     if t[i]==t[i+1]:
        #         t1+=1
        #     if t1==s1:
        #         continue
            
        #     else:
        #         return False
            
        return True
