class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        initial=[i for i in range(1,m+1)]
        print(initial)
        ans=[]
        for i in queries:
            # print(i)
            ind=initial.index(i)
            initial.pop(ind)
            initial.insert(0,i)
            ans.append(ind)
        return (ans)
