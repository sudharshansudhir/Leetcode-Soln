class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        f=-1
        for i in range(len(word)):
            if(word[i]==ch):
                a=word[:i+1]
                return a[::-1]+word[i+1:]
        return word
