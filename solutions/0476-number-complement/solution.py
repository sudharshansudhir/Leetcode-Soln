class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num)[2:]
        bb=""
        for i in b:
            if i=="1":
                bb+="0"
            else:
                bb+="1"
        return int(bb,2)
