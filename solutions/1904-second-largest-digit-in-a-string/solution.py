class Solution:
    def secondHighest(self, s: str) -> int:
        num=[]
        for i in s:
            if i.isdigit():
                if int(i) not in num:
                    num.append(int(i))
        num.sort(reverse=True)
        if(len(num)<=1):
            return -1
        
        return num[1]
