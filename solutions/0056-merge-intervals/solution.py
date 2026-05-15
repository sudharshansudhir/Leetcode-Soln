class Solution:
    def merge(self, s: List[List[int]]) -> List[List[int]]:
        s.sort()
        arr=[s[0]]
        for i in range(1,len(s)):
            if s[i][0]<=arr[-1][1]:
                if s[i][1]>=arr[-1][1]:
                    arr[-1][1]=s[i][1]
            else:
                arr.append(s[i])
        return arr
