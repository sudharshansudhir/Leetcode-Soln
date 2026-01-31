class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ind=ord(target)
        for i in letters:
            if ord(i)>ind:
                return i
        return letters[0]
