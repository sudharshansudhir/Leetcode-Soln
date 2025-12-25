class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd=[]
        even=[]
        for i in range(1,n*2,2):
            odd.append(i)
        for i in range(0,n*2,2):
            even.append(i)
        s1=sum(odd)
        s2=sum(even)
        print(s1,s2,odd,even)
        for i in range(n,-1,-1):
            if(s1%i==0 and s2%i==0):
                return i

