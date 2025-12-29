class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if(ruleKey=="type"):
            ind=0
        elif(ruleKey=="color"):
            ind=1
        else:
            ind=2
        ans=[]
        for item in items:
            if(item[ind]==ruleValue):
                ans.append(item)
        return len(ans)

