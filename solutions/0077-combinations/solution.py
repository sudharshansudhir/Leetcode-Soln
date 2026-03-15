class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr=[]
        pref=[]
        def backtrack(curr):
            # pref=list(set(pref))
            # pref.sort()
            if len(pref)==k:
                arr.append(pref[:])
                return
            for i in range(curr,n+1):
                pref.append(i)
                backtrack(i+1)
                pref.pop()
        backtrack(1)
        return arr




