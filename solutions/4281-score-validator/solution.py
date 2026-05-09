class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        s=0
        w=0
        for i in events:
            if i in ["0","1","2","3","4","5","6"]:
                s+=int(i)
            elif i in ["NB","WD"]:
                s+=1
            elif i=="W":
                if w<10:
                    w+=1
            if w==10:
                break
        return [s,w]
