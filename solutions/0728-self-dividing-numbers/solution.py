class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        s=[]
        for i in range(left,right+1):
            i=str(i)
            flag=True
            for e in i:
                if not e=="0":
                    if not int(i)%int(e)==0:
                        flag=False
                        break
                else:
                    flag=False
                    break
            if flag:
                s.append(int(i))
        return s
