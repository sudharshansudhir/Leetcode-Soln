class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans=[]
        dict={}
        for i in range(len(heights)):
            dict[heights[i]]=names[i]
        heights.sort(reverse=True)
        for i in heights:
            ans.append(dict[i])
        return ans

