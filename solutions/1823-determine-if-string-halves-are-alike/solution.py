class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        one=s[:len(s)//2]
        two=s[len(s)//2:]
        # print(one,two)
        v1=[]
        v2=[]
        for i in one:
            if i.lower() in "aeiou":
                v1.append(i)
        for i in two:
            if i.lower() in "aeiou":
                v2.append(i)
        print(v1,v2)
        if(len(v1)==len(v2)):
            return True
        return False
        # return True
