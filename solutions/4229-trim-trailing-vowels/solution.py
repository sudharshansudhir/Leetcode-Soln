class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        # s=list(s)
        s=s[::-1]
        for i in range(len(s)):
            if s[i] in "aeiou":
                continue
            return s[i:][::-1]
        return ""
