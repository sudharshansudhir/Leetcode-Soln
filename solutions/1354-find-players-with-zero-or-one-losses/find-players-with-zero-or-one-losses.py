class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict={}

        for i in matches:
            dict[i[1]]=dict.get(i[1],0)+1
        # print(dict)
        loss=set()
        for k,v in dict.items():
            if v==1:
                loss.add(k)
        loss=list(loss)
        loss.sort()
        
        wins=set()
        for i in matches:
            if i[0] not in dict.keys():
                wins.add(i[0])
        wins=list(wins)
        wins.sort()
        return [wins,loss]


