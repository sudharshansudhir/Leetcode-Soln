class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l=s.split()
        a=""
        for i in range(k):
            a+=l[i]
            a+=" "
        return a.strip()
