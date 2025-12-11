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
        return True
