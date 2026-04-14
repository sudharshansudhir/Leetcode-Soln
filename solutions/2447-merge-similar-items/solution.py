class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        c={}
        for i in items1:
            if i[0] not in c.keys():
                c[i[0]]=i[1]
            else:
                c[i[0]]+=i[1]
        for i in items2:
            if i[0] not in c.keys():
                c[i[0]]=i[1]
            else:
                c[i[0]]+=i[1]
        newar=[]
        for i in c:
            newar.append([i,c[i]])
        newar.sort()
        return newar
        
