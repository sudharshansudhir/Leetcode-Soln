class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        d=0
        
        for i in range(left,right+1):
            s=bin(i)[2:]

            flag=True
            ones=s.count("1")
            # print(ones)
            # print(s)
            if ones>1:
                for j in range(2,int(ones**0.5)+1):
                    if ones%j==0:
                        flag=False
            else:
                flag=False
            if flag:
                d+=1
        return d

