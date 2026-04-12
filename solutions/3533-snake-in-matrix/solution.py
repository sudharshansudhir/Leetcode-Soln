class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        c=0
        arr=[]
        for i in range(n):
            t=[]
            for j in range(n):
                t.append(c)
                c+=1
            arr.append(t)
        i=0
        j=0
        for each in commands:
            if each=="UP":
                i=i-1
            elif each=="DOWN":
                i+=1
            elif each=="RIGHT":
                j+=1
            else:
                j-=1
        return arr[i][j]
