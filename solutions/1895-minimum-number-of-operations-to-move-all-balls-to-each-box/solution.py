class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        for i in range(len(boxes)):
            t=0
            for j in range(len(boxes)):
                a=0
                if not i==j:
                    if(not boxes[j]=="0"):
                        a+=(int(boxes[j])*abs(j-i))
                    if(a):
                        t+=a
            ans.append(t)
        return (ans)

