class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start=paths[0][0]
        # r1=paths[0][1]
        dict={}
        for i in paths:
            dict[i[0]]=i[1]
        while start in dict.keys():
            start=dict[start]
        return start
