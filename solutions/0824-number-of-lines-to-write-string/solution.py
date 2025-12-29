class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        ans=[]
        a1=""
        c=0

        for i in s:
            ind=ord(i)-97
            c+=widths[ind]
            # print(ind,end=". ")
            if(c<101):
                a1+=i
            else:
                c=0
                c+=widths[ind]
                ans.append(a1)
                a1=""
                a1+=i
        if(a1):
            ans.append(a1)
        return [len(ans),c]
        #  [len(ans),len(ans[-1])]
