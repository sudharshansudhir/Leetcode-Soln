class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d=edges[0][0]
        t=edges[0][1]
        s=0
        e=0
        for i in edges:
            if d in i:
                s+=1
            if t in i:
                e+=1
        if(len(edges)==s):
            return d
        return t
