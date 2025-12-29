class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in details:
            # ph=i[:10]
            # g=i[10]
            age=i[11:13]
            # seat=i[13:]
            if(int(age)>60):
                c+=1
        return c

