class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        a=ord(target)
        for i in letters:
            if(ord(i)>a):
                return i
        return letters[0]
