class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=""
        for i in s:
            ans+=i.lower()
        return ans
