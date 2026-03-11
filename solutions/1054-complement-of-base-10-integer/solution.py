class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b=bin(n)[2:]
        bb=""
        for i in b:
            if i=="1":
                bb+="0"
            else:
                bb+="1"
        return int(bb,2)
