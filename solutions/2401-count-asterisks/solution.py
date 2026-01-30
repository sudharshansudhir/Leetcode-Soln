class Solution:
    def countAsterisks(self, s: str) -> int:
        a=""
        flag=True
        for i in s:
            if i=="|":
                flag=not flag
            if flag:
                a+=i
        return a.count("*")
