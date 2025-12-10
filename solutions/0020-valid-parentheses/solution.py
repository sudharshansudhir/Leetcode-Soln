class Solution:
    def isValid(self, s: str) -> bool:
        open=[]
        close=[]
        c=-1
        for i in s:
            if i in ")]}" and open:
                last=open[-1]
                if (last=="[" and i=="]"):
                    c+=1
                elif(last=="{" and i=="}"):
                    c+=1
                elif(last=="(" and i==")"):
                    c+=1
                else:
                    return False
                open.pop(-1)
            else:
                open.append(i)

        if not(len(open)==len(close)):
            return False
        # close=close[::-1]
        # for i in range(len(open)):
        #     if (open[i]=="[" and close[i]=="]"):
        #         c+=1
        #     elif(open[i]=="{" and close[i]=="}"):
        #         c+=1
        #     elif(open[i]=="(" and close[i]==")"):
        #         c+=1
        #     else:
        #         return False
        return True
