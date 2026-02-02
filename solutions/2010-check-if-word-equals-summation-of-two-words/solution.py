class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        fw=""
        sw=""
        tw=""
        for i in firstWord:
            fw+=str(ord(i)-97)
        for i in secondWord:
            sw+=str(ord(i)-97)
        for i in targetWord:
            tw+=str(ord(i)-97)
        if int(fw)+int(sw)==int(tw):
            return True
        return False

