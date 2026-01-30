class Solution:
    def isBalanced(self, num: str) -> bool:
        a1=[]
        a2=[]
        for i in range(0,len(num),2):
            a1.append(int(num[i]))
            
        for i in range(1,len(num),2):
            a2.append(int(num[i]))
        return sum(a1)==sum(a2)
        
            
