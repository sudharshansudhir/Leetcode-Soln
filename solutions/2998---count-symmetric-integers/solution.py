class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c=0
        for i in range(low,high+1):
            word=str(i)
            if(len(word)%2==0):
                first=word[0:len(word)//2]
                second=word[len(word)//2:]
                s1=0
                s2=0
                for i in first:
                    s1+=int(i)
                for i in second:
                    s2+=int(i)
                if(s1==s2):
                    c+=1
        return c
                    
