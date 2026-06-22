class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text)<7:
            return 0
        dict={
            "b":0,
            "a":0,
            "l":0,
            "o":0,
            "n":0,
        }

        for i in text:
            if i in dict.keys():
                dict[i]+=1
        c=float('inf')
        key=""
        for k,v in dict.items():
            if k=="l" or k=="o":
                v=v//2
            if v<c:
                c=v
                key=k
        for i,j in dict.items():
            if j==0:
                return 0
            if i=="l" or i=="o":
                if j<2:
                    return 0
        if not c==float('inf'):
            return c
        