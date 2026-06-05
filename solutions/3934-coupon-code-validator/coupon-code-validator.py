class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ans=[]
        i=0
        n=len(code)
        while i<n:
            cf=True
            bf=True
            af=True
            c=0
            for e in code[i]:
                if e.isalnum() or e=="_":
                    c+=1
            # print(c,len(code[i]))
            if not c==len(code[i]) or not code[i]:
                cf=False
                i+=1
                continue
            
            if businessLine[i] not in ["electronics", "grocery", "pharmacy", "restaurant"]:
                bf=False
                i+=1
                continue
            if not isActive[i]:
                i+=1
                continue
            ans.append([code[i],businessLine[i]])
            i+=1
        # print(ans)
        ans.sort(key=lambda x:(x[1],x[0]))
        # ans.sort(key=lambda x:x[0])
        print(ans)
        res=[]
        for i in ans:
            res.append(i[0])
        return res