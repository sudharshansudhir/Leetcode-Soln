class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right=[0]
        left=[0]
        j=0
        answer=[]
        for i in range(0,len(nums)-1):
            t=left[j]+nums[i]
            left.append(t)
            j+=1
        j=0
        for i in range(len(nums)-1,0,-1):
            l=right[j]+nums[i]
            right.append(l)
            j+=1
        rt=[]
        for k in range(len(right)-1,-1,-1):
            rt.append(right[k])
        for i in range(len(left)):
            if(left[i]>rt[i]):
                a=left[i]-rt[i]
                answer.append(a)
            else:
                a=rt[i]-left[i]
                answer.append(a)
        return answer


