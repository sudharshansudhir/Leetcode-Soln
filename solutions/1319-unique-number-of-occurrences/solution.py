class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ans=[]
        for i in arr:
            if(arr.count(i) not in ans):
                ans.append(arr.count(i))
        s=list(set(arr))
        if(len(ans)==len(s)):
            return True
        return False
