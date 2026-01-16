class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in image:
            t=i[::-1]
            e=[]
            for tt in t:
                if tt==0:
                    e.append(1)
                else:
                    e.append(0)
            ans.append(e)
        return(ans)
