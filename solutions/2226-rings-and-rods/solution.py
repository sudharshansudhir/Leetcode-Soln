class Solution:
    def countPoints(self, rings: str) -> int:
        dict={}
        for i in range(1,len(rings),2):
            if rings[i] not in dict.keys():
                dict[rings[i]]=[rings[i-1]]
            else:
                g=dict[rings[i]]
                if rings[i-1] not in g:
                    g.append(rings[i-1])
        c=0
        for key in dict:
            # print(dict[key])
            if len(dict[key])==3:
                c+=1
        return c
