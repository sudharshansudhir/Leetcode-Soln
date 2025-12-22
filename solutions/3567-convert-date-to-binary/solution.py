class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ans=date.split("-")
        res=""
        for i in ans:
            res+=bin(int(i))[2:]
            res+="-"
        print(res)
        return res[:len(res)-1]
