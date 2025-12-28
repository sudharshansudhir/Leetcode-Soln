class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ma=""
        if(len(num)==3):
            c=0
            for i in num:
                if(i==num[0]):
                    c+=1
            if(c==3):
                return num
        for i in range(len(num)-2):
            a=num[i:i+3]
            c=0
            print(a)
            for j in a:
                if(j==a[0]):
                    c+=1
            if(c==3):
                if not ma:
                    ma=num[i:i+3]
                elif(int(ma)<int(num[i:i+3])):
                    ma=num[i:i+3]
        return ma
