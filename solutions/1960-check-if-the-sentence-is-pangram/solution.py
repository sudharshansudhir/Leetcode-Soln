class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=""
        for i in sentence:
            # print(i,s)
            if not i in s:
                s+=i
        alp=26
        
        if(len(s)==26):
            return True
        return False
