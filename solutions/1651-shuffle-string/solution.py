class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=""
        dict={}
        for i in range(len(indices)):
            dict[indices[i]]=s[i]
        for i in range(len(s)):
            ans+=dict[i]
        return ans
