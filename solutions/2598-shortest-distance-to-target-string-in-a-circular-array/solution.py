class Solution:
    def closestTarget(self, words: List[str], target: str, ind: int) -> int:
        if ind>len(words):
            return -1
        m1=words[:ind][::-1]+words[ind:][::-1]
        m2=words[ind:]+words[:ind]
        if target not in m1:
            return -1
        return min(m1.index(target)+1,m2.index(target))
        # m2=words[ind:]
        # if target in m1:
        #     i1=m1.index(target)

        # s=float('inf')
        # for i in range(ind,len(words)):


