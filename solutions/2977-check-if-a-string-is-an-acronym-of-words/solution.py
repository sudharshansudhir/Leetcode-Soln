class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ac=""
        for i in words:
            ac+=i[0]
        if(ac==s):
            return True
        return False
